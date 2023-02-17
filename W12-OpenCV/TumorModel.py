######################################
#####Read Images And Make DataSet#####
######################################
import cv2 as cv
import glob
import imutils
import numpy as np
import pandas as pd

yes=glob.glob('./data/yes/*')
no=glob.glob('./data/no/*')

def prepare_image(image: np.ndarray):
    ####Crop####
    gray_image=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_image=cv.GaussianBlur(gray_image,(5,5),0)

    thresh=cv.threshold(gray_image,45,255,cv.THRESH_BINARY)[1]
    thresh=cv.erode(thresh, None,iterations=2)
    thresh=cv.dilate(thresh, None, iterations=2)

    cnts=cv.findContours(thresh.copy(),cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    c=max(cnts,key=cv.contourArea)

    extLeft=tuple(c[c[:,:,0].argmin()][0])
    extRight=tuple(c[c[:,:,0].argmax()][0])
    extTop=tuple(c[c[:,:,1].argmin()][0])
    extBot=tuple(c[c[:,:,1].argmax()][0])

    new_image=image[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

    #resize
    return cv.resize(new_image, (128,128), interpolation=cv.INTER_AREA)

def images_to_list(list_of_image: list, data_list: list, target: int):
    for file_path in list_of_image:
        # Read Image
        img=cv.imread(file_path)
        #Change Dimension from 2 to 1
        row=prepare_image(img).reshape(-1)
        #Add Target
        row=np.append(row,[target])
        data_list.append(row)

data=[]
try:
    images_to_list(yes, data, 1)
    images_to_list(no, data, 0)
except Exception as e:
    print(str(e))

df=pd.DataFrame(data)


####################
#####Make Model#####
####################
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def make_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)

    y_predict= model.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test, y_predict))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_predict))

#####SVC Model#####
print("#####SVC Model#####")
model = make_pipeline(preprocessing.StandardScaler(),SVC(class_weight='balanced'))
make_model(model,X_train, y_train, X_test, y_test)

#####Logistic Model#####
print("#####Logistic Model#####")
lg= LogisticRegression(class_weight='balanced')
make_model(lg,X_train, y_train, X_test, y_test)

#####KNN Model#####
print("#####KNN Model#####")
knn=KNeighborsClassifier(n_neighbors=7)
make_model(knn, X_train, y_train, X_test, y_test)

#####Random Forest#####
print("#####Random Forest#####")
rf=RandomForestClassifier(n_estimators=50, max_samples=20,max_features=9,class_weight='balanced')
make_model(rf, X_train, y_train, X_test, y_test)


#OutPut WithOut Crop
"""
#####SVC Model#####
Accuracy:  0.7555555555555555
Confusion Matrix:
[[ 8  7]
 [ 4 26]]
#####Logistic Model#####
Accuracy:  0.7333333333333333
Confusion Matrix:
[[ 9  6]
 [ 6 24]]
#####KNN Model#####
Accuracy:  0.6888888888888889
Confusion Matrix:
[[ 7  8]
 [ 6 24]]
#####Random Forest#####
Accuracy:  0.6666666666666666
Confusion Matrix:
[[ 5 10]
 [ 5 25]]
 """

#OutPut With Crop
"""
#####SVC Model#####
Accuracy:  0.6444444444444445
Confusion Matrix:
[[ 7  8]
 [ 8 22]]
#####Logistic Model#####
Accuracy:  0.7555555555555555
Confusion Matrix:
[[10  5]
 [ 6 24]]
#####KNN Model#####
Accuracy:  0.6888888888888889
Confusion Matrix:
[[12  3]
 [11 19]]
#####Random Forest#####
Accuracy:  0.6
Confusion Matrix:
[[ 2 13]
 [ 5 25]]
"""