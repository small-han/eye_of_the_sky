# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:32:48 2020

@author: hp
"""

# import asyncio
# import websockets
# #Imageprocessing library
# import numpy as np
# import os
# import nest_asyncio
# nest_asyncio.apply()

# #Function which encodes the image to a string format

# #these function called when the websocket server starts
# async def Operate_soc():
#     #replace with your server ip address and port number
#     uri = "ws://121.40.165.18:8800"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             greet = await websocket.recv()
#             print(greet)
#             filename = await websocket.recv()
#             print(filename)
#             filesize = await websocket.recv()
#             print(filesize)
#             BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
#             path = os.path.join(BASE_DIR, filename)

#             # f = open(path, 'ab')  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
#             # data =await websocket.recv()  # 一次从服务端接收1024字节的数据
#             # f.write(data)  # 写入
#             # f.close()  # 关闭文件


# #run the client untill the function complete
# asyncio.get_event_loop().run_until_complete(Operate_soc())


# import asyncio
# import websockets
# import nest_asyncio
# nest_asyncio.apply()
# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# start_server = websockets.serve(hello, "121.40.165.18", 8800)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()



# import asyncio
# import websockets
# import nest_asyncio
# import time
# nest_asyncio.apply()
# async def hello():
#     uri = "ws://121.40.165.18:8800"
#     async with websockets.connect(uri) as websocket:
#         # name = "yu"

#         # await websocket.send(name)
#         # print(f"> {name}")

#         greeting = await websocket.recv()
#         print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()




import asyncio
import websockets
import nest_asyncio
import os
nest_asyncio.apply()
async def hello(websocket, path): 
    
    greeting="hello"
    await websocket.send(greeting.encode('utf-8'))
    print(greeting)
    
    img_name = "pic.png"  # 将客户端传输过来的图片名称（bytes）解码成字符串
    await websocket.send(img_name.encode('utf-8'))
    print(img_name)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PIC_DIR = os.path.join(BASE_DIR, 'pics')
    img_path = os.path.join(PIC_DIR, img_name)  # 获得对应图片的绝对路径
    file_size = str(os.stat(img_path).st_size)  # 获得图像文件的大小，字节单位
    await websocket.send(str(file_size).encode('utf-8'))
    print(file_size)
    f = open(img_path, 'rb')
    file = f.read(int(file_size))
    print("read")
    await websocket.send(file)#.encode())

    print('上传成功')
    


start_server = websockets.serve(hello, "localhost", 6668)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()