import aiohttp
import asyncio

async def send_greeting(port):
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.sleep(1)
            await session.post(f'http://localhost:{port}/post', data="Hello world", headers={'Content-Type': 'Greeting'})


def start_webclient():
    loop = asyncio.get_event_loop()
    port_list = [8080, 8081, 8082]
    for port in port_list:
        loop.create_task(send_greeting(port))

    loop.run_forever()
