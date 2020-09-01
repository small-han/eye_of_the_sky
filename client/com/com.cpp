#include "com.h"


void Transmitter::init(){
    ws = WebSocket::from_url(serverAddress);
    if(ws==NULL)
    {
        std::cout<<"Error Server Address"<<std::endl;
        assert(ws);
    } 
}


void Transmitter::send(FileType type, std::string data, uint32_t size){
    switch(type)
    {
        case FileType::String:
            ws->send(data);
            break;
        case FileType::Binary:
            ws->send(data);
            data="../data/"+data;
            std::ifstream is(data, std::ifstream::in | std::ios::binary);
            if(is.bad())
                std::cout<<"can't read image"<<data;
            // 2. 计算图片长度
            is.seekg(0, is.end);
            int length = is.tellg();
            is.seekg(0, is.beg);
            std::string str_length=std::to_string(length);
            // std::cout<<str_length;
            ws->send(str_length);
            // 3. 创建内存缓存区
            char * buffer = new char[length];
            // 4. 读取图片
            is.read(buffer, length);
            // 到此，图片已经成功的被读取到内存（buffer）中
            std::string str_data(buffer,buffer+length);
            // std::cout<<"size:"<<str_data.length()<<std::endl;
            delete [] buffer;
            ws->sendBinary(str_data);
            is.close();

    }
}

void Transmitter::recv(){
    while (ws->getReadyState() != WebSocket::CLOSED) {
      ws->poll(10);
      ws->dispatch(handler);
    }
 
}

void Transmitter::handler(const std::string &message)
{
    printf(">>> %s\n", message.c_str());
}
