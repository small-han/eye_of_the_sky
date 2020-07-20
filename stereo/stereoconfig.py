# -*- coding: utf-8 -*- 
import numpy as np
 
# 双目相机参数
class stereoCamera1(object):
    def __init__(self):
        # 左相机内参
        self.cam_matrix_left = np.array([[1652.6, 49.8588, 408.8597],
                                         [0., 2165.6, -61.4078],
                                         [0., 0., 1.]])
        # 右相机内参
        self.cam_matrix_right = np.array([[1395.3, -29.3097, 392.662],
                                          [0., 1799.9, -2.3723],
                                          [0., 0., 1.]])
 
        # 左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[0.5065, 0.3872, -0.1803, -0.0681, 0]])
        self.distortion_r = np.array([[0.2319, 0.0857, -0.1054, -0.0094, 0]])
 
        # 旋转矩阵
        self.R = np.array([[0.9981, 0.0433, 0.0445],
                           [-0.0431, 0.9991, -0.0046],
                           [-0.0447, 0.0027, 0.9990]])
 
        # 平移矩阵
        self.T = np.array([[-7.0679], [-3.8084], [-13.4170]])
 
        # 焦距
        #self.focal_length = 1602.46406  # 默认值，一般取立体校正后的重投影矩阵Q中的 Q[2,3]
 
        # 基线距离
        #self.baseline = 14.0679  # 单位：mm， 为平移向量的第一个参数（取绝对值）