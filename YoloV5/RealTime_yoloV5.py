import torch
import numpy as np 
import cv2

class ObjectDetection:

    def __init__(self):
        self.model = self.load_model()
        self.classes = self.model.names
        # Check the system use cpu or GPU
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print('Device Used:',self.device)

    
    def load_model(self):
        # Load yolov5 model

        model=torch.hub.load('ultralytics/yolov5','yolov5s',pretrained=True)
        return model

    def score_frame(self,frame):
        # Make score frame
        self.model.to(self.device)
        frame=[frame]
        result=self.model(frame)

        labels,cord=result.xyxyn[0][: ,-1] ,result.xyxyn[0][:,:-1]
        return labels,cord

    def class_to_label(self,x):
        return self.classes[int(x)]


    def plot_box(self,result,frame):
        # Try to make a boundry box
        labels,cord=result
        n=len(labels)
        x_shape,y_shape=frame.shape[1],frame.shape[0]
        for i in range(n):
            row=cord[i]
            if row[4]>=0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame


detection = ObjectDetection()
# activate webcam and predict with yolov5
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    result=detection.score_frame(frame)
    frame=detection.plot_box(result,frame)

    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()

cv2.destroyAllWindows()




        

