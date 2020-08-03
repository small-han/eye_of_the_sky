# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:53:21 2020

@author: hp
"""
import socket
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import pandas as pd
import sys
import time
import socket
import os


IP="192.168.3.10"
port=6669
DIR=os.path.dirname(os.path.abspath(__file__))


class Receive(QThread):
    signal = pyqtSignal()

    def __init__(self):
        super(Receive, self).__init__()
        self.IP=IP
        self.port=port
        self.DIR=DIR
        # self.signal.connect(?)
        
    def __del__(self):
        self.wait()

    def run(self):
        while 1:
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
            self.signal.emit()
        
        client.close()

class UI(QWidget):
    print('1')
    def __init__(self,parent=None):
        super(UI,self).__init__(parent)
        print('2')
        self.thread=Receive()
        self.thread.signal.connect(self.initUI)
        self.thread.start()
        print('3')
        # self.initUI()

    def initUI(self):
 
        app = QApplication(sys.argv) 
        grid = QGridLayout()  
        
        lab1=QLabel()
        lab1.setPixmap(QPixmap('pic.png'))
        grid.addWidget(lab1, 0, 0, 1, 4)
        
        
        info=pd.read_csv('info.csv',encoding="gbk")
        info=info.fillna('')
        k=info.values
        for i in range(len(info)):
            for j in range(4):
                k[i,j]=str(k[i,j])
        # names=k[0,:]
        col=['语义信息', '坐标', '距离', '社交距离']
        k=np.vstack((col,k))
        
        for i in range(len(info)+1):
            for j in range(4):
                if k[i,j]!='':
                    grid.addWidget(QPushButton(k[i,j]),i+2,j)
        grid.setSpacing(20)
        self.setLayout(grid)   
        
        self.setGeometry(150, 80, 900, 1000)  
        self.setWindowTitle('JETBOT')
        self.show()

if __name__ == '__main__':
    w = UI()

    sys.exit(app.exec_())
