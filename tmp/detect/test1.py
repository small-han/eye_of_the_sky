import jetson.inference
import jetson.utils
import numpy as np
import cv2
import time

class Detection:
    
    def __init__(self,network="ssd-mobilenet-v2",width=1080,height=720,overlay="box,labels,conf"):
        self.net = jetson.inference.detectNet(network, threshold=0.5)
        self.camera = jetson.utils.gstCamera(width ,height, "0")
        self.camera2 = jetson.utils.gstCamera(width ,height, "1")
        self.overlay=overlay
        
    def Detect(self,camera="left"):
        if camera is "left":
            img, self.width, self.height = self.camera.CaptureRGBA(zeroCopy=1)
        else:
            img, self.width, self.height = self.camera2.CaptureRGBA(zeroCopy=1)
        detections = self.net.Detect(img, self.width, self.height,self.overlay)
        return detections,img

    def Save_Image(self,file_name,img):
        #jetson.utils.saveImageRGBA(file_name, img, self.width, self.height)
        conv1 = jetson.utils.cudaToNumpy(img, self.width, self.height, 4)        
        #print(time.time())
        conv2 = cv2.cvtColor(conv1, cv2.COLOR_RGBA2RGB).astype(np.uint8)
        #print(time.time())
        conv3 = cv2.cvtColor(conv2, cv2.COLOR_RGB2BGR)
        #print(time.time())
        cv2.imwrite(file_name,conv3)
        #print(time.time())

    
    def Save_Data(self,file_name,detections):
        with open(file_name,"a")as f:
            f.write(str(time.time())+" "+str(len(detections))+"\n")
            for dec in detections:
                f.write(self.net.GetClassDesc(dec.ClassID)+" ")
                f.write(str(dec.Confidence)+" ")
                f.write(str(dec.Top)+" ")
                f.write(str(dec.Bottom)+" ")
                f.write(str(dec.Left)+" ")
                f.write(str(dec.Right)+"\n")
