import torch
import cv2
import numpy as np

# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


img = cv2.imread('img.jpg')


img = cv2.resize(img, (640, 640))
img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, HWC to CHW
img = np.ascontiguousarray(img)
img = torch.from_numpy(img).float()
img /= 255.0

results = model(img)


img = cv2.imread('img.jpg')
for i in range(len(results.xyxy[0])):
    x1, y1, x2, y2, conf, cls = results.xyxy[0][i]
    label = model.names[int(cls)]
    color = (0, 255, 0)  # green
    thickness = 2
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
    cv2.putText(img, f"{label}: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
