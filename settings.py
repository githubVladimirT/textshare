import dotenv
import logging

DOMAIN = "0.0.0.0"
PORT = 7443
PREF = "https://"
DEBUG = False
LIVETIME = 2 * 86400
POSTS_DIR = "posts"
POSTS_OLD_DIR = "posts.old"
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"
LOGS_DIR = "logs"
LOG_LEVEL = logging.INFO
SITE_TITLE = "TextShare"
KEY = dotenv.get_key('.env', 'KEY')
HTTPS = {
    'cert': "./certs/cert.pem",
    'key': "./certs/key.pem"
}
