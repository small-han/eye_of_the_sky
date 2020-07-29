#include "com.h"


void Transmitter::init(){
    ws = WebSocket::from_url(serverAddress);
    if(ws==NULL)
    {
        std::cout<<"Error Server Address"<<std::endl;
        assert(ws);
    } 
}


void Transmitter::send(FileType type, uint8_t* buf, uint32_t size){
        ws->send("goodbye");
}

void Transmitter::recv(){
    while (ws->getReadyState() != WebSocket::CLOSED) {
      ws->poll(10);
      ws->dispatch(handler);
    }
 
}

void Transmitter::handler(const std::string &message){
{
    printf(">>> %s\n", message.c_str());
    if (message == "world") { ws->close(); }
}