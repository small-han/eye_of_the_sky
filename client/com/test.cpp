#include "com.h"
int main()
{
    Transmitter my_trans=Transmitter("ws://192.168.43.8:8765");
    my_trans.init();
    // my_trans.send(my_trans.FileType::String,"hello",0);
    my_trans.send(my_trans.FileType::Binary,"outL.jpg",0);
    my_trans.recv();
}