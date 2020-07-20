# -*- coding: utf-8 -*- 
import cv2
import numpy as np
import time
import stereoconfig

class steroMeasure():
    def __init__(self):
        self.iml = 0  # 左图
        self.imr = 0  # 右图
        self.Q = 0  # 右图
        self.config = stereoconfig.stereoCamera1() # load camera config

    def setInputArray(self,iml,imr):
        self.iml = iml   # 左图
        self.imr = imr   # 右图
        height, width = self.iml.shape[0:2]
        map1x, map1y, map2x, map2y, self.Q= self.getRectifyTransform(height, width, self.config)  # 获取用于畸变校正和立体校正的映射矩阵以及用于计算像素空间坐标的重投影矩阵

    def setInputPath(self,iml,imr):
        self.iml = cv2.imread(iml)   # 左图
        self.imr = cv2.imread(imr)   # 右图
        height, width = self.iml.shape[0:2]
        map1x, map1y, map2x, map2y, self.Q= self.getRectifyTransform(height, width, self.config)  # 获取用于畸变校正和立体校正的映射矩阵以及用于计算像素空间坐标的重投影矩阵

    def preprocess(self,img1,img2):
        # 彩色图->灰度图
        im1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        im2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # 直方图均衡
        # im1 = cv2.equalizeHist(im1)
        # im2 = cv2.equalizeHist(im2)
        return im1,im2

    # 消除畸变
    def undistortion(self, image, camera_matrix, dist_coeff):
        undistortion_image = cv2.undistort(image, camera_matrix, dist_coeff)
        return undistortion_image
    
    # 获取畸变校正和立体校正的映射变换矩阵、重投影矩阵
    # @param：config是一个类，存储着双目标定的参数:config = stereoconfig.stereoCamera()
    def getRectifyTransform(self,height, width, config):
        # 读取内参和外参
        left_K = config.cam_matrix_left
        right_K = config.cam_matrix_right
        left_distortion = config.distortion_l
        right_distortion = config.distortion_r
        R = config.R
        T = config.T
        # 计算校正变换
        R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(left_K, left_distortion, right_K, right_distortion, (width, height), R, T, alpha=0)
        map1x, map1y = cv2.initUndistortRectifyMap(left_K, left_distortion, R1, P1, (width, height), cv2.CV_32FC1)
        map2x, map2y = cv2.initUndistortRectifyMap(right_K, right_distortion, R2, P2, (width, height), cv2.CV_32FC1)
        return map1x, map1y, map2x, map2y, Q
    
    # 畸变校正和立体校正
    def rectifyImage(self, image1, image2, map1x, map1y, map2x, map2y):
        rectifyed_img1 = cv2.remap(image1, map1x, map1y, cv2.INTER_AREA)
        rectifyed_img2 = cv2.remap(image2, map2x, map2y, cv2.INTER_AREA)
        return rectifyed_img1, rectifyed_img2
    
    
    # 视差计算
    def disparity_SGBM(self, left_image, right_image, down_scale=False):
        # SGBM匹配参数设置
        if left_image.ndim == 2:
            img_channels = 1
        else:
            img_channels = 3
        blockSize = 11
        param = {'minDisparity': 0,
                'numDisparities': 128,
                'blockSize': blockSize,
                'P1': 8 * img_channels * blockSize ** 2,
                'P2': 32 * img_channels * blockSize ** 2,
                'disp12MaxDiff': 1,
                'preFilterCap': 63,
                'uniquenessRatio': 15,
                'speckleWindowSize': 100,
                'speckleRange': 1,
                'mode': cv2.STEREO_SGBM_MODE_SGBM_3WAY
                }

        # 构建SGBM对象
        sgbm = cv2.StereoSGBM_create(**param)
        # 计算视差图
        size = (left_image.shape[1], left_image.shape[0])
        if down_scale == False:
            disparity_left = sgbm.compute(left_image, right_image)
        else:
            left_image_down = cv2.pyrDown(left_image)
            right_image_down = cv2.pyrDown(right_image)
            factor = size[0] / left_image_down.shape[1]
            disparity_left_half = sgbm.compute(left_image_down, right_image_down)
            disparity_left = cv2.resize(disparity_left_half, size, interpolation=cv2.INTER_AREA) 
            disparity_left *= factor 
        return disparity_left, None
    
    def run(self):
        # 立体匹配
        iml_, imr_ = self.preprocess(self.iml, self.imr)   # 预处理，不做也可以
        disp, _ = self.disparity_SGBM(iml_, imr_)   # 这里传入的是未经立体校正的图像，因为我们使用的middleburry图片已经是校正过的了
        disp = np.divide(disp.astype(np.float32), 16.)  # 除以16得到真实视差（因为SGBM算法得到的视差是×16的）
        msg = cv2.imwrite('./out.png', disp)
        # 计算像素点的3D坐标（左相机坐标系下）
        points_3d = cv2.reprojectImageTo3D(disp, self.Q)  # 可以使用上文的stereo_config.py给出的参数
        return points_3d # return location

if __name__ == '__main__':
    node = steroMeasure()
    node.setInputPath("./data/aloeL.jpg","./data/aloeR.jpg")
    s = time.time()
    for i in range(10):
        node.run()
    e = time.time()
    print(e-s)