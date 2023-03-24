import dotenv
import logging

DOMAIN = "vladimir.selfip.ru"
HOST = "0.0.0.0"
PRIVATE_PORT = 7443
#PORT = 80
PREF = "https://"
DEBUG = True #False
LIVETIME = 2 * 86400
POSTS_DIR = "posts"
POSTS_OLD_DIR = "posts.old"
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"
LOGS_DIR = "logs"
LOG_LEVEL = logging.DEBUG
SITE_TITLE = "TextShare"
KEY = dotenv.get_key('.env', 'KEY')
HTTPS = {
    'cert': "./certs/cert.pem",
    'key': "./certs/key.pem"
}
