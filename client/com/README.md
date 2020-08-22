生成可执行文件并执行
> g++ com.cpp ./easywsclient/easywsclient.cpp test.cpp -o out && ./out 

会得到如下结果
> \>>> 您发送的消息是:hello

> \>>> 您发送的消息是:../data/outL.jpg

> \>>> 您发送的消息是:1027176

> \>>> 您发送的消息是:����

第一次发送了“hello”，第二次发送图片名字，第三次发送大小，第四次发送二进制文件
+ 如果要改变服务器ip，在test.cpp第4行改变ip
if want to run test.cpp,have to modify the address of easywsclient.hpp in com.h