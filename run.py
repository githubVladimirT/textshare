from hypercorn.config import Config
from hypercorn.asyncio import serve
import settings
import asyncio
from server import app

config = Config()
config.bind = [f'{settings.DOMAIN}:{settings.PORT}']
config.loglevel = 'WARNING'
config.certfile = settings.HTTPS['cert']
config.keyfile = settings.HTTPS['key']
config.debug = settings.DEBUG

asyncio.run(serve(app, config))