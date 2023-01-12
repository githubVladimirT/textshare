import os
from time import time
from uuid import uuid4

from flask import Flask, Response, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages
from settings import *

app = Flask(
    __name__, static_folder=f"./{STATIC_DIR}", template_folder=f"./{TEMPLATES_DIR}")
app.config.from_object(__name__)
flatpages = FlatPages(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = KEY


@app.route('/')
def index():
    return render_template("index.html", site_title=SITE_TITLE)


@app.route('/', methods=["POST"])
def index_post():
    now = time()

    for file in os.listdir(POSTS_DIR):
        if os.path.getmtime(os.path.join(POSTS_DIR, file)) < now - LIVETIME:
            if os.path.isfile(os.path.join(POSTS_DIR, file)):
                os.remove(os.path.join(POSTS_DIR, file))

    del now

    text = request.form.get('text')

    if text.strip() != "":

        curr_uuid = uuid4()
        path = '{}/{}'.format(POSTS_DIR, curr_uuid)

        with open(path, 'w') as file:
            file.write(text)

        return redirect(url_for("index", url=f"{PREF}{DOMAIN}:{PORT}/post/{curr_uuid}"))
    else:
        return render_template("index.html", redir="false")


@app.route('/post/<uuid>/')
def post(uuid):
    path = '{}/{}'.format(POSTS_DIR, uuid)

    with open(path, 'r') as file:
        post = file.read()

    return Response(post, mimetype='text/plain')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=DOMAIN, port=PORT, debug=DEBUG,
            ssl_context=(HTTPS['cert'], HTTPS['key']))

    # app.run(host=DOMAIN, port=PORT, debug=DEBUG)
