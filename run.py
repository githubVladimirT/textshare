from hypercorn.config import Config
from hypercorn.asyncio import serve
import settings
import asyncio
from server import app

config = Config()
config.bind = [f'{settings.HOST}:{settings.PRIVATE_PORT}']
#config.loglevel = 'WARNING'
config.loglevel = 'DEBUG'
# config.certfile = settings.HTTPS['cert']
# config.keyfile = settings.HTTPS['key']
config.debug = settings.DEBUG

asyncio.run(serve(app, config))
