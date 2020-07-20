import cv2
import numpy as np
import time
from stereo.Stereo import steroMeasure
from stereo.StereoConfig import stereoCamera1

class Robot():
    def __init__(self):
        # TODO: invoke camera api
        self.3DLocationLeft = 0
        self.imgL = 0
        self.imgR = 0
    
    def 3DLocate(self):
        measure = steroMeasure()
        measure.setInputArray(self.imgL,self.imgR)
        self.3DLocationLeft = node.run()

    def detect(self):
        # invoke detection class to detect human body
        self.targets = [] # output target  

    def label(self):
        for index1 in range(len(self.targets)):
            for index2 in range(index1, len(self.targets)):
                # calculate distance between bodies
                # output unqualified data 
                # label data in image

    def transer(self):
        #TODO:invoke transfer class to transfer result to serverside 



