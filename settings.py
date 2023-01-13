import dotenv
import logging

DOMAIN = "172.16.1.33"
PORT = 7443
PREF = "https://"
# DEBUG = True
LIVETIME = 2 * 86400
POSTS_DIR = "posts"
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"
LOGS_DIR = "logs"
LOG_LEVEL = logging.INFO
SITE_TITLE = "TextShare"
KEY = dotenv.get_key('.env', 'KEY')
# HTTPS = {
# 'cert': "./certs/cert.pem",
# 'key': "./certs/key.pem"
# }
