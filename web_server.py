import asyncio
from aiohttp import web
loop = asyncio.get_event_loop()

class Server():
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.app=web.Application()

    async def get(self):
        return web.Response(text='Hello from port 8080')

    async def post(self,request):
        try:
            print(f'Greeting string from client host name: {request.host}, and Message: {await request.text()}')
        except Exception as ex:
            print(f'ERROR: {ex.__str__()}')
        #stop server after receive request from client
        await self.stop()
        return web.Response(text='Testing...')

    async def start_site_with_post(self):

        self.app.add_routes([web.get('/get', self.get),web.post('/post', self.post)])
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()

        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()
    async def stop(self):
        await self.runner.shutdown()
        await self.site.stop()
        await self.app.shutdown()


def start_webserver():
    ports = [8080, 8081, 8082]
    for port in ports:
        app = Server("localhost", port)
        loop.create_task(app.start_site_with_post())
"""
        try:
            loop.run_forever()
        except:
            pass
        finally:
            print('All server are stops')
"""

