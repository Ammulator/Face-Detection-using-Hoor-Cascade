import cv2
alg="haarcascade_frontalface_default"
haar = cv2.CascadeClassifier(alg)#file will be loaded
#initilaze the camera
cam = cv2.VideoCapture(2)
#Frame and Uptil Camera Feed

while True:
    _,Cimg=cam.read()#Get the frame
    grayImg=cv2.cvtColor(Cimg,cv2.COLOR_BGR2GRAY)
    faces=haar.detectMultiScale(grayImg,1.3,3)#Lot of coordinates of the face.
    #to find x and y coordinates of the face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",img)
    key=cv2.waitKey(10)
    if key=="27":#Esc button to release the camera.
        break
cam.release()
cv2.destroyAllWindows()
    
