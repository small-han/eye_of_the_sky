#include"soc.h"
using namespace std;
/*
uint32_t int32_IP(char *IP)
{
        int l=0,r=0;
        int int32IP=0;
        int x=1;
        char component[10];
        for(r;r<strlen(IP);r++)
        {

                if(IP[r]=='.'||r == strlen(IP)-1)
                {
                        int i=0;
                        for(i;i<r-l;i++)
                        {
                                component[i]=IP[l+i];
                        }
                        component[r-l]='\0';
                        int32IP+= atoi(component)*x;
                        x*=256;
                        l=r+1;
                        if(r==strlen(IP)-1)
                        {
                                break;
                        }
                }


        }
        return int32IP;
}

void com()
{
        Socket *my_socket=Socket::Create(SOCKET_TCP);
        char* remoteIP = "192.168.43.169";
        uint16_t remotePort = 6661;

        my_socket->Bind("192.168.43.16",3332);
        std::cout<<"Bind success"<<std::endl;
        my_socket->Connect(remoteIP,remotePort);
        std::cout<<"Connect success"<<std::endl;
        uint8_t buf1[1000];
        my_socket->Recieve(buf1,1000);
        std::cout<<buf1<<std::endl;
        ifstream in("/home/jetbot/eye_of_the_sky/client/data/out.jpg",ios::in|ios::binary);
        in.seekg(0,ios::end);
        streampos ps=in.tellg();
        string str="out.jpg";
        str+="|";
        str+=std::to_string(int(ps));
//usr/local/include/jetson-utils/

        const char *c_str = str.c_str();

        char *buf2 = new char[strlen(c_str)+1];
        strcpy(buf2,c_str);

        my_socket->Send(buf2,strlen(c_str),int32_IP(remoteIP),remotePort);
        in.open("/home/jetbot/eye_of_the_sky/client/data/out.jpg",ios::in|ios::binary);
        char *data_buf=new char[int(ps)];
        cout<<int(ps)<<endl;
        in.read(data_buf,int(ps));
        for(int i=0;i<100;i++)
                cout<<int(data_buf[i]);
        my_socket->Send(data_buf,ps,int32_IP(remoteIP),remotePort);

        char *data_buf=new char[int(ps)];
        FILE *fp = fopen("/home/jetbot/eye_of_the_sky/client/data/out.jpg","rb");
        if( fp == NULL)
        {
                cout<<"error"<<endl;
        }
        else
        {
                fread(data_buf,int(ps),1,fp);
                my_socket->Send(data_buf,ps,int32_IP(remoteIP),remotePort);
        }
	delete buf2;
	delete data_buf;
}
*/
Comm::Comm()
{
	port=1234;
}
uint32_t Comm::int32_IP(char *IP)
{
        int l=0,r=0;
        int int32IP=0;
        int x=1;
        char component[10];
        for(r;r<strlen(IP);r++)
        {

                if(IP[r]=='.'||r == strlen(IP)-1)
                {
                        int i=0;
                        for(i;i<r-l;i++)
                        {
                                component[i]=IP[l+i];
                        }
                        component[r-l]='\0';
                        int32IP+= atoi(component)*x;
                        x*=256;
                        l=r+1;
                        if(r==strlen(IP)-1)
                        {
                                break;
                        }
                }


        }
        return int32IP;
}
void Comm::run()
{
	Socket* my_socket=Socket::Create(SOCKET_TCP);
	remoteIP = "192.168.43.169";
        remotePort = 6661;
	my_socket->Bind("192.168.43.16",port);
	port+=1;
	port=port%10000+1234;
	my_socket->Connect(remoteIP,remotePort);
        std::cout<<"Connect success"<<std::endl;
        uint8_t buf1[1000];
        my_socket->Recieve(buf1,1000);
        std::cout<<buf1<<std::endl;
        ifstream in("/home/jetbot/eye_of_the_sky/client/data/out.jpg",ios::in|ios::binary);
        in.seekg(0,ios::end);
        streampos ps=in.tellg();
        string str="out.jpg";
        str+="|";
        str+=std::to_string(int(ps));
//usr/local/include/jetson-utils/

        const char *c_str = str.c_str();

        char *buf2 = new char[strlen(c_str)+1];
        strcpy(buf2,c_str);

        my_socket->Send(buf2,strlen(buf2),int32_IP(remoteIP),remotePort);
/*
        in.open("/home/jetbot/eye_of_the_sky/client/data/out.jpg",ios::in|ios::binary);
        char *data_buf=new char[int(ps)];
        cout<<int(ps)<<endl;
        in.read(data_buf,int(ps));
        for(int i=0;i<100;i++)
                cout<<int(data_buf[i]);
        my_socket->Send(data_buf,ps,int32_IP(remoteIP),remotePort);
*/

        char *data_buf=new char[int(ps)];
        FILE *fp = fopen("/home/jetbot/eye_of_the_sky/client/data/out.jpg","rb");
        if( fp == NULL)
        {
                cout<<"error"<<endl;
        }
        else
        {
                fread(data_buf,int(ps),1,fp);
                my_socket->Send(data_buf,ps,int32_IP(remoteIP),remotePort);
        }
        delete buf2;
        delete data_buf;
	my_socket->~Socket();


}

