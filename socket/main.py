import asyncio
import websockets
import datetime
import random
import sys

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def show_time():
    try:
        with open('ttyrecord','rb') as file:
            while True:
                byte = file.read(1)
                if byte:
                    print(byte)
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