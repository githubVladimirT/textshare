from decouple import config
import dotenv

DOMAIN = "0.0.0.0"
PORT = 7443
PREF = "https://"
DEBUG = True
POSTS_DIR = "posts"
LIVETIME = 2 * 86400
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"
SITE_TITLE = "Copypaste"
KEY = dotenv.get_key('.env', 'KEY')
HTTPS = {
    'cert': "./cert/cert.pem",
    'key': "./cert/key.pem"
}

