from flask import request

from ..app import app
from .controllers import (
    list_all_articles_controller,
    retrieve_article_controller
)


@app.route("/articles", methods=["GET"])
def list_articles():
    if request.method == "GET":
        return list_all_articles_controller()
    else:
        return "Method is Not Allowed"


@app.route("/articles/<article_id>", methods=["GET"])
def retrieve_articles(article_id):
    if request.method == "GET":
        return retrieve_article_controller(article_id)
    else:
        return "Method is Not Allowed"
