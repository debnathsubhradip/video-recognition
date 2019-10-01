import cv2 as c
import time
face_cascade=c.CascadeClassifier("haarcascade_frontalface_default.xml")
img=c.imread("galaxy.jpg",-1)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces :
    img=c.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    time.sleep(3)
    font = c.FONT_HERSHEY_SIMPLEX

print(type(img))
print(img)
print(img.shape)
print(img.ndim)
r_img=c.resize(img,(1920,800))
print(r_img.shape)
c.imshow("Galaxy",r_img)
c.imwrite("Galaxy_resized.jpg",r_img)
c.waitKey(0)
c.destroyAllWindows()