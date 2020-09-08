# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:08:03 2020

@author: hp
"""


import socket
import os
import sys
from PyQt5 import QtWidgets,QtGui
import pandas as pd

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
import pandas as pd

import time

import random
import string
import asyncio
import websockets
from PyQt5.QtCore import pyqtSignal

client_ip="localhost"
client_port=6668
server_ip="localhost"
server_port=6668



class SocketServer(QThread):
    trigger = pyqtSignal(str)
    def __int__(self):
        super(QThread, self).__init__()

    def run(self):
        # trigger = pyqtSignal(str)
        print('run')
        while(1):
            IP="localhost"
            port=6664
            DIR=os.path.dirname(os.path.abspath(__file__))
            client = socket.socket()  # 1.声明协议类型，同时生成socket链接对象
            client.bind((IP, port))  # 绑定要监听端口=(服务器的ip地址+任意一个端口)
            client.listen(5)  # 监听
            print("waiting for connection...")
            conn, addr = client.accept()  # 等电话打进来
                # conn就是客户端连过来而在服务器端为其生成的一个连接实例
            print("收到来自{}请求".format(addr))

            BASE_DIR = DIR  # 获得当前目录

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
            self.trigger.emit(str(time.time()))
        
        # client.close()
        

class Server():
    def __init__(self):#,IP,port,DIR):
        self.app = QApplication(sys.argv)
        # print('1')
        # self.IP=IP
        # self.port=port
        # self.DIR=DIR
        # UI类
        self.mainwindow = QtWidgets.QMainWindow()
        self.centuralLayout = QHBoxLayout()
        self.UI = QWidget() # UI
        
        self.dataWidget = QWidget() # data plan UI
        self.table = QTableWidget() # data table
        self.dataLayout = QVBoxLayout()
        self.picLabel = QLabel()
        self.setDataLayout()

        self.buttonsWidget = QWidget() # buttons
        self.buttonLayout = QFormLayout()
        self.setButtonLayout()

        self.initCenturalWidget()

        self.initMainWindow() # main window

        # worker 异步传递消息
        self.socketWorker  = SocketServer()
        #self.socketWorker  = SocketServer(self.IP,self.port,self.DIR)
        self.socketWorker.trigger.connect(self.refreshUI)

    def initMainWindow(self):
        self.mainwindow.setCentralWidget(self.UI)    
        self.mainwindow.statusBar().showMessage('Running')
        self.mainwindow.resize(QDesktopWidget().availableGeometry().size() * 0.6);
        self.mainwindow.setWindowTitle('Sky Eyes')


    def setDataLayout(self):
        self.picLabel = QLabel()
        self.picLabel.setPixmap(QPixmap('pic.png'))
        self.picLabel.setAlignment(Qt.AlignCenter)
        self.picLabel.setScaledContents(True)
        self.picLabel.setMinimumHeight(500)
        self.dataLayout.addWidget(self.picLabel)
        self.table.horizontalHeader().setFixedHeight(50) ##设置表头高度
        # self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)#设置第五列宽度自动调整，充满屏幕
        self.table.horizontalHeader().setStretchLastSection(True) ##设置最后一列拉伸至最大[]
        # table.setSelectionMode(QAbstractItemView.SingleSelection) #设置只可以单选，可以使用ExtendedSelection进行多选
        # table.setSelectionBehavior(QAbstractItemView.SelectRows) #设置 不可选择单个单元格，只可选择一行。
        # self.table.horizontalHeader().resizeSection(0,200) #设置第一列的宽度为200

        self.table.setColumnCount(4)##设置表格一共有4列
        self.table.setHorizontalHeaderLabels(['ID', 'Location', 'Distance', 'Social-Distance'])#设置表头文字
        self.table.horizontalHeader().setSectionsClickable(False) #可以禁止点击表头的列
        # table.sortItems(1,Qt.DescendingOrder) #设置按照第二列自动降序排序
        self.table.horizontalHeader().setStyleSheet('QHeaderView::section{background:green}')#设置表头的背景色为绿色
        # self.table.setColumnHidden(1,True)#将第二列隐藏
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置表格不可更改
        self.table.setSortingEnabled(True)#设置表头可以自动排序
        self.dataLayout.addWidget(self.table)
        self.dataWidget.setLayout(self.dataLayout)

    def setButtonLayout(self):
        clientIPBtn = QPushButton("Client IP");
        clientIPEdit = QLineEdit()
        clientIPEdit.textChanged.connect(self.ClientIP)
        clientIPEdit.setPlaceholderText(str(client_ip))
        
        clientPortBtn = QPushButton("Client Port");
        clientPortEdit = QLineEdit()
        clientPortEdit.textChanged.connect(self.ClientPort)
        clientPortEdit.setPlaceholderText(str(client_port))
        
        serverIPBtn = QPushButton("Server IP");
        serverIPEdit = QLineEdit()
        serverIPEdit.textChanged.connect(self.ServerIP)
        serverIPEdit.setPlaceholderText(str(server_ip))
        
        serverPortBtn = QPushButton("Server Port");
        serverPortEdit = QLineEdit()
        serverPortEdit.textChanged.connect(self.ServerPort)
        serverPortEdit.setPlaceholderText(str(server_port))
         # add start button
        button1 = QPushButton('Start')
        button1.setMinimumHeight(100)
        button1.setMinimumWidth(100)
        button1.clicked.connect(self.start)
        button2 = QPushButton('Close')
        button2.setMinimumHeight(100)
        button2.setMinimumWidth(100)
        button2.clicked.connect(QCoreApplication.instance().quit)
        # button2.clicked.connect(sys.exit(0))
        # button2.clicked.connect(self.close())
        
        # auto vectical scale
        buttons = [button1,button2,clientIPBtn,clientIPEdit,clientPortBtn,clientPortEdit,serverIPBtn,serverIPEdit,serverPortBtn,serverPortEdit]
        for btn in buttons:
            policy = btn.sizePolicy()
            policy.setVerticalStretch(1)
            btn.setSizePolicy(policy)
        
        self.buttonLayout.addRow(button1, button2)
        self.buttonLayout.addRow(clientIPBtn, clientIPEdit)
        self.buttonLayout.addRow(clientPortBtn, clientPortEdit)
        self.buttonLayout.addRow(serverIPBtn, serverIPEdit)
        self.buttonLayout.addRow(serverPortBtn, serverPortEdit)
        self.buttonLayout.setVerticalSpacing(80)
                
        self.buttonLayout.setAlignment(Qt.AlignLeft)
        self.buttonsWidget.setLayout(self.buttonLayout)
    
    def ClientIP(self,text):
        client_ip=str(text)
    def ClientPort(self,text):
        client_port=int(text)
    def ServerIP(self,text):
        server_ip=str(text)
    def ServerPort(self,text):
        server_port=int(text)
    
    def initCenturalWidget(self):
        self.centuralLayout.setSpacing(20)
        self.centuralLayout.addWidget(self.dataWidget,95)
        self.centuralLayout.addWidget(self.buttonsWidget,5)
        self.UI.setLayout(self.centuralLayout) # 
        self.UI.setAutoFillBackground(True)
        # init background color
        color = "grey"
        palette = self.UI.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.UI.setPalette(palette)

    def add_one_line(self,oneLine):
        assert(len(oneLine)==4)
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        for idx,data in enumerate(oneLine):
            self.table.setItem(row,idx,QTableWidgetItem(data))

    def update_data(self):
        # self.table.clear()
        # self.table.setRowCount(0)
        info=pd.read_csv('pics/info.csv',encoding="gbk")
        info=info.fillna('')
        k=info.values
        for i in range(len(info)):
            for j in range(4):
                k[i,j]=str(k[i,j])
        for i in range(len(info)):
            oneline = []
            for j in range(4):
                oneline.append(k[i,j])
            self.add_one_line(oneline)

    def updatePic(self):
        self.picLabel.setPixmap(QPixmap('pic.png'))
        # if random.randint(1,100)%2==0:
        #     self.picLabel.setPixmap(QPixmap('pic.png'))
        # else:
        #     self.picLabel.setPixmap(QPixmap('pic.png'))
            
    def refreshUI(self):
        self.update_data()
        self.updatePic()

    def start(self):
        self.socketWorker.start()
        self.mainwindow.show()
        sys.exit(self.app.exec_())

    '''
    add a line to the table. only for testing!!!!!!
    '''
    def add_line_test(self):
        # self.table.cellChanged.disconnect()
        idx = self.get_random_string(8)
        loc = str(random.randint(1,10))
        distance = str(random.randint(1,10))
        soc = str(random.randint(2,3))
        self.add_one_line([idx,loc,distance,soc])
    
    '''
    generate random string. only for testing
    '''
    def get_random_string(self,length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

if __name__ == "__main__":
    # IP = "127.0.0.1"
    # port = 6669
    # DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')

    server = Server()#IP,port,DIR)
    server.start()
    
