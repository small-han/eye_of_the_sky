#include "easywsclient.hpp"
//#include "easywsclient.cpp" // <-- include only if you don't want compile separately
#include <assert.h>
#include <stdio.h>
#include <string>
#include <memory>
#include <vector>
#include <iostream>
#include <fstream>

#include <assert.h>
#include <stdio.h>
#include <string>

using easywsclient::WebSocket;


class Transmitter{
    public:
        enum class FileType{String, Binary};
        Transmitter();
        Transmitter(std::string address):serverAddress(address) {};
        ~Transmitter(){
            if(ws != NULL)
            {
                ws->close();
                delete ws;
            }
        };
        void init();
        void send(FileType type, std::string data, uint32_t size);
        void recv();
    private:
        std::string serverAddress;
        WebSocket::pointer ws;
        static void handler(const std::string& message);
};