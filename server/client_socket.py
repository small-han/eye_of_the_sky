# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:03:45 2020

@author: hp
"""

# -*- coding=utf-8 -*-
import socket
import os


class Send:
    def __init__(self,IP,port):
        self.IP=IP
        self.port=port
    
    def send_data(self):

        conn = socket.socket()  # 声明socket类型，同时生成socket连接对象
        conn.connect((self.IP,self.port))  # 链接服务器的ip + 端口
        print("connected!")
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获得当前目录
        PIC_DIR = os.path.join(BASE_DIR, 'pics')  # 图片文件夹的路径
        pic_names = sorted(os.listdir(PIC_DIR))  # 获得排序后的所有图片名称，放在一个列表中【'1.jpg','2.jpg',...,'9.jpg'】
        # 将图片名称放进一个大字符串中
        pic_names = " ".join(i for i in pic_names)  # '0.jpg 1.jpg 2.jpg 3.jpg 4.jpg 5.jpg 6.jpg 7.jpg 8.jpg 9.jpg'
        

        while True:
            data = conn.recv(1024)  # 接收数据，获取图像名称的命令，指定需要传输的图片
            print(data)
    
            if not data:
                print("client has lost...")
                break
            if data.decode('utf-8') == 'get pics_names':  # 获取图像名称的命令  定义为get pics_names
                conn.send(pic_names.encode('utf-8'))
            elif data.decode('utf-8') == 'break':
                break
            else:
                img_name = data.decode('utf-8')  # 将客户端传输过来的图片名称（bytes）解码成字符串
                img_path = os.path.join(PIC_DIR, img_name)  # 获得对应图片的绝对路径
                file_size = os.stat(img_path).st_size  # 获得图像文件的大小，字节单位
                file_info = '%s|%s' % (img_name, file_size)
                conn.sendall(file_info.encode('utf-8'))#conn.sendall(bytes(file_info, 'utf-8'))
    
                f = open(img_path, 'rb')  # 以二进制格式打开一个文件用于只读
                has_sent = 0  # 记录下已经发送的字节数
                while has_sent != file_size:  # 发送的字节数 不等于 图像的大小，则接着发送
                    file = f.read(1024)  # 一次读1024个字节
                    conn.sendall(file)  # 发送给客户端
                    has_sent += len(file)  # 更新已发送的字节数
                f.close()  # 发送结束，关闭文件
                print('上传成功')
       
        
        conn.close()
        
        
IP="localhost"
port=6664
sen=Send(IP,port)
sen.send_data()
