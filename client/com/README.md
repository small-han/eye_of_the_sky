## com
+ Transmitter(std::string address):serverAddress(address) ;

    输入要连接的远端的地址，开始构建类
+ void init();

    与远端进行连接
+ void send(FileType type, std::string data, uint32_t size);
    type指发送二进制或者string数据。如要发送二进制文件，data表示二进制文件地址，如要发送string，data就是string数据。size暂时没用
+ recv();
  调用recv则等待远端发送数据，远端如果发送了数据调用hander函数。