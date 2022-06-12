import asyncio
import websockets
import datetime
import random
import sys
import screen

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def readBytes(file, length) -> bytes:
    data = b''
    while True:
        nb = file.read(1)
        if not nb == b'':
            data += nb
            if len(data) == length:
                return data


async def readTTY(file, cb):
    while True:
        sec = int.from_bytes(await readBytes(file, 4), 'little')
        usec = int.from_bytes(await readBytes(file, 4), 'little')
        length = int.from_bytes(await readBytes(file, 4), 'little')
        data = await readBytes(file, length)
        cb(data.decode('utf-8'),sec, usec)

async def show_time():
    term = screen.Terminal()
    try:
        with open('ttyrecord','rb') as file:
            await readTTY(file, lambda x,y,z: term.print(x))
                    # message = datetime.datetime.utcnow().isoformat()
                    # websockets.broadcast(CONNECTIONS, message)
                    # await asyncio.sleep(random.random()*2+1)
    except FileNotFoundError:
        print('no recording found!',file=sys.stderr)



async def main():
    async with websockets.serve(register, 'localhost', 8082):
        await show_time()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)