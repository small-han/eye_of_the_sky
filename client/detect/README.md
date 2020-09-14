## detect
###  成员
+ detectNet *net;

    神经网络
+ gstCamera *camera_left;

    左摄像头
+ gstCamera *camera_right;

    右摄像头

+ float *imgRGBA_left;

    左摄像头图片
+  float *imgRGBA_right;
  
    右摄像机图片

+ detectNet::Detection *detections;
    
    识别出来的detection数组
+ int numDetections;
   
    识别出来的detection个数
### 函数
+   detect();
  
    加载神经网络SSD_MOBLIENET_V2，初始化摄像头
+   ~detect();

+   void CaptureRGBA();

    获取摄像头RGBA图片保存到imgRGBA_left,imgRGBA_right
    
+   void detect_left();

    detect左摄像头，将识别出的数据放在*detections，识别的个数放在numDetections.
    Detection类参见
    https://rawgit.com/dusty-nv/jetson-inference/dev/docs/html/structdetectNet_1_1Detection.htm
    
+ std::string Get_ID(int index);

    输入index，获取对应detection的ID，例如人就是"person",书就是“book”

+ void Get_Pos(int index, float &top, float &down, float &left, float &right);

    输入index，获取对应detection的上下左右坐标，以左下角为原点，像素为单位
+ void OverLay_Left(int index);

  此函数是jetson提供，存在bug，在stereo中用opencv重新实现

+   void Save_RGBA(std::string left_str,std::string right_str);
    
    输入图片保存地址，保存图片
