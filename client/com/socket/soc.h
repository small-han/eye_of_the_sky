#include <jetson-utils/Socket.h>
#include <string>
#include <string.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

class Comm
{
public:
	Comm();

//	Socket *my_socket;
	int port;
	char* remoteIP ;
        uint16_t remotePort ;
	uint32_t int32_IP(char *IP);
	void run();


};
