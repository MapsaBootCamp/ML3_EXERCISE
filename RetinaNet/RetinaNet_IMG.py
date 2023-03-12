# The goal of the exercise is trying to take a picture from Webcam and save it as a png image and..
# ..detect the object with RetinaNet keras

# Download the requiries of Retinanet:
# 1.git clone https://github.com/fizyr/keras-retinanet.git
   # cd keras-retinanet/
   # pip install .
   # python setup.py build_ext --inplace

## Download the resnet50_coco_best
# 2.urllib.request.urlretrieve('https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5', 'resnet50_coco_best_v2.1.0.h5')

## Download the coco lables
# 3.urllib.request.urlretrieve('https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt', 'coco-labels-paper.txt')


# Import required libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import urllib
from urllib import request
import os
import cv2
from PIL import Image
from keras_retinanet import models
from keras_retinanet.utils.image import preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color


# Make a model with retinanet
model = models.load_model('resnet50_coco_best_v2.1.0.h5')

# Make a list of coco dataset categorizes 
class_labels = [label.rstrip() for label in open("coco-labels-paper.txt")]

# A function for taking a picture from camera and save it 
def Take_photo():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed to take a photo
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed to exit the camera and saving the image
            img_name = "cv_{}.png".format(img_counter)
            # save an image as png format
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))  
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

# The function for drawing boundry box
def detect_draw_bounding_boxes(img_path, threshold=0.6):
    # Read image 
    img = np.array(Image.open(img_path))
    print(f"Shape of the image: {img.shape}")
    
    # Remove the alpha channel from image 
    img = img[:,:,:3]
    
    # Preprocess and resize - mean subtraction and scaling 
    img_proc = preprocess_image(img)
    img_proc, scale = resize_image(img_proc)
    
    print(f"Shape of the pre processed image: {img_proc.shape}")
    
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(img_proc, axis=0))
    
    # Stadardize the boxes 
    boxes /= scale
    
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        
        if score < threshold:
            break
        
        box = box.astype(np.int32) 
        color = label_color(label)
        draw_box(img, box, color=color)
        
        
        class_label = class_labels[label]
        caption = f"{class_label} {score:.3f}"
        draw_caption(img, box, caption)
    plt.axis('off')
    plt.imshow(img)
    plt.show()

Take_photo()
# only take one photo as cv_0.png in each run 
detect_draw_bounding_boxes('cv_0.png')