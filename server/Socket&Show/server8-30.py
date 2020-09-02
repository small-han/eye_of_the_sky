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
import sys
import time
import socket
import os
import random
import string
import asyncio
import websockets

async def trans(websocket, path):
    print("web start")
    while True:
        # BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        #文件名
        filename = await websocket.recv()
        print(filename)
        #文件大小
        filesize = await websocket.recv()
        filesize = int(filesize)
        print(filesize)
        
        path = os.path.join(BASE_DIR, filename)
        f = open(path, 'wb') 
        #接收文件
        data =await websocket.recv() 
        f.write(data)
        f.close()  
        trigger.emit(str(time.time()))
        print("receive successfully!")

class SocketServer(QThread):
    trigger = pyqtSignal(str)
    def __int__(self):
        super(QThread, self).__init__()

    def run(self):
        print('run')
        start_server = websockets.serve(trans, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        # self.trigger.emit(str(time.time()))
        

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
        clientPortBtn = QPushButton("Client Port");
        clientPortEdit = QLineEdit()
        serverIPBtn = QPushButton("Server IP");
        serverIPEdit = QLineEdit()
        serverPortBtn = QPushButton("Server Port");
        serverPortEdit = QLineEdit()
         # add start button
        button1 = QPushButton('Start')
        button1.setMinimumHeight(100)
        button1.setMinimumWidth(100)
        button2 = QPushButton('Close')
        button2.setMinimumHeight(100)
        button2.setMinimumWidth(100)

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