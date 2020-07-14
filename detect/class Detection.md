## class Detection

###  \__init__ (……):

+ 默认参数：

  + network=“ssd-mobilnet-v2”

    选择要使用的网络

  + length=1080

    长度

  + width=720

    宽度

  + overlay=“box,labels,conf”

    overlay参数控制最终图像的显示，box表示有框体，labels表示有识别信息，conf表示有准确度。

### Detect（）：

对摄像头的拍摄进行识别

+ return：

  + detections：

    detections是一个list,list的每一项代表了探测的对象，每一个对象是一个类，类包含的参数如下：

    + Area
          Area of bounding box
    + Bottom
          Bottom bounding box coordinate
    + Center
          Center (x,y) coordinate of bounding box
    + ClassID
          Class index of the detected object，
    + Confidence
          Confidence value of the detected object
    + Height
          Height of bounding box
    + Instance
          Instance index of the detected object
    + Left
          Left bounding box coordinate
    + Right
          Right bounding box coordinate
    + Top
          Top bounding box coordinate
    + Width
           Width of bounding box

  + img

    这里的lmg并不是正常的图片格式，需要用Save_Image进行保存

### Save_Image():

保存图片

+ 输入：
  + file_name：保存图片的路径
  + img：Detect()返回的img

### Save_Date():

+ 输入：
  + file_name:保存数据的路径
  + detections:Detect()返回的detections
+ 存储的数据结构：
  + 第一行：时间 识别出的物体数
  + 第二行：识别的语义信息 准确度 上坐标 下坐标 左坐标 右坐标

更多函数参见：https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.html