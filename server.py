import os
from time import time
from uuid import uuid4

import logger
from quart import Quart, Response, render_template, request, redirect, url_for
from settings import *

app = Quart(
    __name__, static_folder=f"./{STATIC_DIR}", template_folder=f"./{TEMPLATES_DIR}")
app.config.from_object(__name__)
# app.config['SECRET_KEY'] = KEY


@app.route('/')
async def index():
    return await render_template("index.html", site_title=SITE_TITLE)


@app.route('/', methods=["POST"])
async def index_post():
    text = (await request.form)['text']

    if text.strip() != "":

        curr_uuid = uuid4()
        path = '{}/{}'.format(POSTS_DIR, curr_uuid)

        with open(path, 'w') as file:
            file.write(text)

        logger.clientslogger(str(request.remote_addr), "POST", str(curr_uuid))

        return redirect(url_for("index", url=f"{PREF}{DOMAIN}:{PORT}/post/{curr_uuid}"))
    else:
        return await render_template("index.html")


@app.route('/post/<uuid>/', methods=["GET"])
async def post(uuid):
    path = '{}/{}'.format(POSTS_DIR, uuid)

    delete_old_posts()

    try:
        with open(path, 'r') as file:
            post = file.read()
        logger.clientslogger(str(request.remote_addr), "GET", uuid)

        return Response(post, mimetype='text/plain')
    except FileNotFoundError:
        return await render_template("404.html"), 404


@app.errorhandler(404)
async def page_not_found(error):
    return await render_template("404.html"), 404


def delete_old_posts():
    now = time()
    for file in os.listdir(POSTS_DIR):
        if os.path.getmtime(os.path.join(POSTS_DIR, file)) < now - LIVETIME:
            if os.path.isfile(os.path.join(POSTS_DIR, file)):
                os.rename(os.path.join(POSTS_DIR, file), os.path.join(
                    POSTS_OLD_DIR, file + "_deleted"))
                logger.clientslogger(str(request.remote_addr), "DELETE", file)
