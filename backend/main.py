from aiohttp import web


async def ping(request):
    print('Ping')
    return web.json_response(data={'a': 'b'})


async def init():
    app = web.Application()
    app.router.add_get("/ping", ping)
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, port=8000)
