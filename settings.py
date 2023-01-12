import dotenv

DOMAIN = "172.16.1.33"
PORT = 7443
PREF = "https://"
DEBUG = True
POSTS_DIR = "posts"
LIVETIME = 2 * 86400
STATIC_DIR = "static"
TEMPLATES_DIR = "templates"
SITE_TITLE = "TextShare"
HOME_NAME = "TxTS"
KEY = dotenv.get_key('.env', 'KEY')
HTTPS = {
    'cert': "./certs/cert.pem",
    'key': "./certs/key.pem"
}
