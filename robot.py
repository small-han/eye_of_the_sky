import cv2
import numpy as np
import time
from detect.HumanDetect import Detection
from stereo.stereo import steroMeasure
from stereo.stereoconfig import stereoCamera1

class Robot():
    def __init__(self):
        # TODO: invoke camera api
        self.LocationLeft = 0
        self.imgL = "./outl.jpg"
        self.imgR = "./outr.jpg"
        self.distance=2000
        self.My_Detection=Detection(width=720,height=480)
    
    def Locate3D(self):
        measure = steroMeasure()
        measure.setInputPath(self.imgL,self.imgR)
        self.LocationLeft = measure.run()

    def detect(self):
        # invoke detection class to detect human body
        my_detectionsL,my_imageL= self.My_Detection.Detect()
        my_detectionsR,my_imageR= self.My_Detection.Detect(camera="right")
        self.My_Detection.Save_Image(self.imgL,my_imageL)
        self.My_Detection.Save_Image(self.imgR,my_imageR)
        self.targets = self.My_Detection.Get_Target(my_detectionsL) # output target  


    def label(self):
        for index1 in range(len(self.targets)):
            for index2 in range(index1, len(self.targets)):
                res1=robot.LocationLeft[int(index1[1])][int(index1[0])]
                res2=robot.LocationLeft[int(index2[1])][int(index2[2])]
                if np.sqrt(pow(res1[0]-res1[0],2)+pow(res2[2]-res2[2],2))<self.distance:
                    return False
        return True
                # calculate distance between bodies
                # output unqualified data 
                # label data in image

    def transer(self):
        pass
        #TODO:invoke transfer class to transfer result to serverside 

if __name__=="__main__":
    robot=Robot()
    robot.detect()
    robot.Locate3D()
    for i in robot.targets:
        print(i)
        print(len(robot.LocationLeft),len(robot.LocationLeft[1]))
        print(robot.LocationLeft[int(i[1])][int(i[0])])



