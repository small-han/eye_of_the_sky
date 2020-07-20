"""
from test1 import Detection
import time
My_Detection=Detection(width=720,height=480)
while True:
    time_before=time.time()
    my_detections,my_image= My_Detection.Detect()
    #my_detections2,my_image2= My_Detection.Detect(camera="right")
    My_Detection.Save_Image("./out.jpg",my_image)
    #My_Detection.Save_Image("./out2.jpg",my_image2)
    My_Detection.Save_Data("./log.txt",my_detections)
    print("time:"+str(time.time()-time_before))
    a=input()
"""
import cv2
cap1=cv2.VideoCapture(0)
ret,frame=cap1.read()
cv2.imwrite("out1.jpg",frame)