## stereo
+ void run(string left_addr,string right_addr);

    输入左图片名和右图片名，计算结果放在lo中
+ bool Compute_Distance(int x1,int y1,int x2,int y2);

    给出两点的坐标，计算两点的距离
+ void Overlay_Red(int top,int bottom,int left,int right);
    输入上下左右的坐标，画上红框

+ void Overlay_Green(int top,int bottom,int left,int right);

    输入上下左右的坐标，画上绿框

+ void Save(std::string addr)
    输入要保存的地址，进行保存