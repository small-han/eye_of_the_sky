# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:52:26 2020

@author: hp
"""

import socket
import os
import sys
from PyQt5 import QtWidgets,QtGui
import pandas as pd

class Receive:
    def __init__(self, IP, port, DIR):
        self.IP=IP
        self.port=port
        self.DIR=DIR
    
    def receive_data(self):
        # client = socket.socket()  # 声明socket类型，同时生成socket连接对象
        # client.connect((self.IP,self.port))  # 链接服务器的ip + 端口
        
        client = socket.socket()  # 1.声明协议类型，同时生成socket链接对象
        client.bind((self.IP, self.port))  # 绑定要监听端口=(服务器的ip地址+任意一个端口)
        client.listen(5)  # 监听
        print("waiting for connection...")
        conn, addr = client.accept()  # 等电话打进来
            # conn就是客户端连过来而在服务器端为其生成的一个连接实例
        print("收到来自{}请求".format(addr))
        
        BASE_DIR = self.DIR  # 获得当前目录
        
        command=['pic.png','info.csv','break']
        for i in range(3):
            msg = command[i]  # 获得要向服务端发送的信息，字符串格式
            if len(msg) == 0:
                continue
        
            conn.sendall(msg.encode('utf-8'))
            # client.send(msg.encode("utf-8"))      # 将字符串格式编码成bytes，发送
            if msg == 'break':
                break
            data = conn.recv(1024)  # 接收服务端返回的内容
            if len(str(data, 'utf-8').split('|')) == 2:  # 如果返回的字符串长度为2，说明针对的任务2，从服务端传回一张图片
                filename, filesize = str(data, 'utf8').split('|')  # 获得指定图像的名称，图像大小
                path = os.path.join(BASE_DIR, filename)  # 指定图像的保存路径
                filesize = int(filesize)  # 图像大小转换成整形
        
                f = open(path, 'ab')  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
                has_receive = 0  # 统计接收到的字节数
                while has_receive != filesize:
                    data1 = conn.recv(1024)  # 一次从服务端接收1024字节的数据
                    f.write(data1)  # 写入
                    has_receive += len(data1)  # 更新接收到的字节数
                f.close()  # 关闭文件
            print("recv:", data.decode())
        
        client.close()

def UI():
    info=pd.read_csv('info.csv',encoding="gbk")
    info=info.fillna('')
    k=info.values
    for i in range(len(info)):
        for j in range(4):
            k[i,j]=str(k[i,j])
    
    s1='语义信息'
    s2='坐标'
    s3='距离'
    s4='社交距离'
    for i in range(len(k)):
        s1=s1+' \n '+k[i,0]
    for i in range(len(k)):
        s2=s2+' \n '+k[i,1]
    for i in range(len(k)):
        s3=s3+' \n '+k[i,2]
    for i in range(len(k)):
        s4=s4+' \n '+k[i,3] 
            
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    w.setGeometry(100,100,1300,900)
    w.setWindowTitle('JRTBOT')
    l0=QtWidgets.QLabel(w)
    png=QtGui.QPixmap('pic.png')
    l0.setPixmap(png)
    
    l1=QtWidgets.QLabel(w)
    l1.setText(s1)
    l2=QtWidgets.QLabel(w)
    l2.setText(s2)
    l3=QtWidgets.QLabel(w)
    l3.setText(s3)
    l4=QtWidgets.QLabel(w)
    l4.setText(s4)
    
    
    #调整l1和l2的位置
    l0.move(100,20)
    l1.move(100,600)
    l2.move(200,600)
    l3.move(300,600)
    l4.move(400,600)
    #显示整个窗口
    w.show()
    #退出整个app
    app.exit(app.exec_())




IP="192.168.3.10"
port=6663
DIR=os.path.dirname(os.path.abspath(__file__))

rev = Receive(IP,port,DIR)
rev.receive_data()
UI()


