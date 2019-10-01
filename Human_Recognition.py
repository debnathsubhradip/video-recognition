import cv2 as c
import time
from datetime import datetime
import os
import gender
import  folder_control as fc
def recognition() :
    face_cascade=c.CascadeClassifier("haarcascade_frontalface_default.xml")
    video = c.VideoCapture(0)
    a=0
    while True :
        dt = datetime.now()
        a=a+1
        check, frame = video.read()
        print(check)
        print(frame)
        gray=frame
        #gray=c.cvtColor(frame,c.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
        # time.sleep(3)
        font = c.FONT_HERSHEY_SIMPLEX
        #Saving the Images


        for x,y,w,h in faces :
            fc.check()
            text = "Human"
            # gray=c.resize(gray,(1024,700))
            gray=c.rectangle(gray, (x,y),(x+w,y+h),(0,255,0),1)
            c.putText(gray, text, (x, h), c.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), lineType=c.LINE_AA)
            crop_image= gray[y:y+h, x:x+w]
            # c.imwrite(
            #     "human" + '_' + str(dt.year) + '_' + str(dt.month) + '_' + str(dt.day) + '_' + str(dt.hour) + '_' + str(
            #         dt.minute) + '_' + str(dt.second) + '_' + str(dt.microsecond) + ".jpg", crop_image)

        c.imshow("Capturing",gray)

        key=c.waitKey(1)
        if key==ord('q'):
            break
    print(a)
    video.release()
    c.destroyAllWindows()

recognition()
