# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:32:48 2020

@author: hp
"""
import asyncio
import websockets
import os
# import nest_asyncio
# nest_asyncio.apply()
async def hello(websocket, path):

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
        
        print("receive successfully!")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



