"""
异步IO模型是所有模型中效率最高的，适用范围最广的
相关模块和框架
模块：asyncio模块
异步框架：sanic tronado twisted
速度快
"""
import threading
import asyncio
import time


async def hello():
    print("hello world %s" % threading.current_thread())
    # yield from asyncio.sleep(1)
    time.sleep(2)
    print("hello world %s" % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
