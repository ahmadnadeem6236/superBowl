from flask import jsonify
from .models import Article
# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522


def list_all_articles_controller():
    articles = Article.query.all()
    response = []
    for article in articles:
        response.append(article.toDict())
    return jsonify(response)


def retrieve_article_controller(article_id):
    response = Article.query.get(article_id).toDict()
    return jsonify(response)


def test_controller():
    print("Scheduler...")