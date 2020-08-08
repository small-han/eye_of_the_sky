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
        #接收问候
        greet = await websocket.recv()
        print(greet)
        #文件名
        filename = await websocket.recv()
        print(filename)
        #文件大小
        filesize = await websocket.recv()
        filesize = int(filesize)
        print(filesize)
        
        # BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(BASE_DIR, filename)
        f = open(path, 'ab') 
        #接收文件
        data =await websocket.recv() 
        f.write(data)
        f.close()  
        print("receive successfully!")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



# async def Operate_soc():
#     # uri = "ws://121.40.165.18:8800"
#     uri = "ws://localhost:6662"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             greet = await websocket.recv()
#             # greet = greet.decode('utf-8')
#             print(greet)
#             filename = await websocket.recv()
#             # filename = filename.decode('utf-8')
#             print(filename)
#             filesize = await websocket.recv()
#             filesize = int(filesize)
#             print(filesize)
            
#             # BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
#             # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#             # path = os.path.join(BASE_DIR, filename)
#             # f = open(path, 'ab')  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
#             # data =await websocket.recv()  # 一次从服务端接收1024字节的数据
#             # f.write(data)#.decode())  # 写入
#             # f.close()  # 关闭文件
#             print("receive successfully!")


# asyncio.get_event_loop().run_until_complete(Operate_soc())
# asyncio.get_event_loop().run_forever()






# import asyncio
# import websockets
# #Imageprocessing library
# import os
# import nest_asyncio
# nest_asyncio.apply()

# async def Operate_soc():
#     # uri = "ws://121.40.165.18:8800"
#     uri = "ws://localhost:6662"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             greet = await websocket.recv()
#             greet = greet.decode('utf-8')
#             print(greet)
#             filename = await websocket.recv()
#             filename = filename.decode('utf-8')
#             print(filename)
#             filesize = await websocket.recv()
#             filesize = int(filesize.decode('utf-8'))
#             print(filesize)
            
#             # BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
#             # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#             # path = os.path.join(BASE_DIR, filename)
#             # f = open(path, 'ab')  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
#             # data =await websocket.recv()  # 一次从服务端接收1024字节的数据
#             # f.write(data)#.decode())  # 写入
#             # f.close()  # 关闭文件
#             print("receive successfully!")

# for i in range(5):
#     asyncio.get_event_loop().run_until_complete(Operate_soc())
#     asyncio.get_event_loop().run_forever()






# import asyncio
# import websockets

# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# start_server = websockets.serve(hello, "localhost", 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()










# import asyncio
# import websockets
# import nest_asyncio
# import os
# nest_asyncio.apply()
# async def hello(websocket, path): 
    
#     greet = await websocket.recv()
#     greet = greet.decode('utf-8')
#     print(greet)
#     filename = await websocket.recv()
#     filename = filename.decode('utf-8')
#     print(filename)
#     filesize = await websocket.recv()
#     filesize = int(filesize.decode('utf-8'))
#     print(filesize)
    
#     # BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
#     # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     # path = os.path.join(BASE_DIR, filename)
#     # f = open(path, 'ab')  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
#     # data =await websocket.recv()  # 一次从服务端接收1024字节的数据
#     # f.write(data)#.decode())  # 写入
#     # f.close()  # 关闭文件
#     # print("receive successfully!")



# start_server = websockets.serve(hello, "localhost", 1234)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


# import asyncio
# import websockets

# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# start_server = websockets.serve(hello, "localhost", 8765)

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
#         name = "yu"

#         await websocket.send(name)
#         print(f"> {name}")

#         greeting = await websocket.recv()
#         print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()



# import asyncio
# import websockets
# import nest_asyncio
# nest_asyncio.apply()

# async def hello():
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         name = input("What's your name? ")

#         await websocket.send(name)
#         print(f"> {name}")

#         greeting = await websocket.recv()
#         print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())
