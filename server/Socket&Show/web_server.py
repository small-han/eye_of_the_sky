# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:32:48 2020

@author: hp
"""

import asyncio
import websockets
import numpy as np
import os
import nest_asyncio
nest_asyncio.apply()

async def Operate_soc():
    uri = "ws://121.40.165.18:8800"
    async with websockets.connect(uri) as websocket:
        while True:
            greet = await websocket.recv()
            print(greet)
            filename = await websocket.recv()
            print(filename)
            filesize = await websocket.recv()
            print(filesize)
            BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pics')
            path = os.path.join(BASE_DIR, filename)

            f = open(path, 'ab') 
            data =await websocket.recv() 
            f.write(data)
            f.close() 


#run the client untill the function complete
asyncio.get_event_loop().run_until_complete(Operate_soc())




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
