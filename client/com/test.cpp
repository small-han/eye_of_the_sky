#include "com.h"
int main()
{
    Transmitter my_trans=Transmitter("ws://www.idcd.com:8866");
    my_trans.init();
    my_trans.send(my_trans.FileType::String,"hello",0);
    my_trans.send(my_trans.FileType::Binary,"outL.jpg",0);
    my_trans.recv();
}