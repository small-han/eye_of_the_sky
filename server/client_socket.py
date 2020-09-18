# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:03:45 2020

@author: hp
"""
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
        while 1:
            data = conn.recv(1024)  # 接收数据，获取图像名称的命令，指定需要传输的图片
            if data.decode('utf-8') == 'break':
                break
            else:
                file_name = data.decode('utf-8')  # 将客户端传输过来的图片名称（bytes）解码成字符串
                file_path = os.path.join(PIC_DIR, file_name)  # 获得对应图片的绝对路径
                file_size = os.stat(file_path).st_size  # 获得图像文件的大小，字节单位
                file_info = '%s|%s' % (file_name, file_size) #将文件名与大小用|拼接"pic.png|372625" "info.csv|84"
                conn.sendall(file_info.encode('utf-8'))#c发送信息
    
                f = open(file_path, 'rb')  # 以二进制格式打开一个文件用于只读
                file = f.read(file_size)  # 全部发送
                conn.sendall(file)  # 发送给客户端
                f.close()  # 发送结束，关闭文件
                print('上传成功')

        conn.close()
        
        
IP="localhost"
port=6668
sen=Send(IP,port)
sen.send_data()
