import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Conv2D, concatenate, UpSampling2D
from tensorflow.keras.models import Model


base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='w.h5')


for layer in base_model.layers:
    layer.trainable = False

base_output = base_model.get_layer('block_16_project_BN').output

decoder_layer1 = UpSampling2D(size=(2,2))(base_output)
decoder_layer2 = Conv2D(128, kernel_size=1, padding='same', activation='relu')(decoder_layer1)
skip_connection1 = base_model.get_layer('block_13_expand_relu').output
decoder_layer3 = concatenate([decoder_layer2, skip_connection1], axis=-1)
decoder_layer4 = UpSampling2D(size=(2,2))(decoder_layer3)
decoder_layer5 = Conv2D(64, kernel_size=1, padding='same', activation='relu')(decoder_layer4)
skip_connection2 = base_model.get_layer('block_6_expand_relu').output
decoder_layer6 = concatenate([decoder_layer5, skip_connection2], axis=-1)
decoder_layer7 = UpSampling2D(size=(2,2))(decoder_layer6)
decoder_layer8 = Conv2D(32, kernel_size=1, padding='same', activation='relu')(decoder_layer7)
decoder_layer9 = Conv2D(1, kernel_size=1, activation='sigmoid')(decoder_layer8)


model = Model(inputs=base_model.input, outputs=decoder_layer9)



model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


print(model.summary())


model.save('person_segmentation_model.h5')


model = tf.keras.models.load_model("person_segmentation_model.h5")


segmentation_layer = tf.keras.layers.Conv2D(1, 1, activation='sigmoid')(model.output)

# Define the model input
model_input = tf.keras.Model(model.input, segmentation_layer)


cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()


    input_image = cv2.resize(frame, (224, 224))
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image / 255.

    output = model_input.predict(input_image)
    mask = cv2.resize(output[0], (frame.shape[1], frame.shape[0]))
    mask = (mask > 0.5).astype(np.uint8)

    # Apply the mask to the frame
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the result
    cv2.imshow('Original', frame)
    cv2.imshow('Masked', masked_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()