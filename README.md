Project Name: SkyEye

Class
1. Detection()
2. steroMeasure()
3. Transfer() #To be confirmed

Calling Procedure:
1. Fetch two images from camera
2. Feed feteched images to Detection to obtain detection of huamna body
3. Feed feteched images to steroMeasure to obtain 3D location of each pixle
4. Label unqualified huamna body in images 
5. Send labeled images to Server side with TransferClass

#TODO

Client: Jetson Nano
Server: Laptop

Server界面部分：
1. 显示内容的缺失 + 界面基本没有设计规划
    缺少的内容: 比如开始按钮，比如停止按钮，显示本机IP，设置本机端口，显示连接的客户端IP+端口，显示通信的内容（文件名，大小等）
    美观方面：widget之间没有布局，简单layout分布，需要使用qt layout对显示的内容仔细布局

2. 异步线程更新界面： 主线程负责界面渲染，子线程负责在后台轮询接收数据（不然就是现在的一次性界面）

Client部分
1. Detect是否能用未知
2. Steoreo引用了新模块，还需要和detect链接还没解决
3. 通信模块尚未还没有

