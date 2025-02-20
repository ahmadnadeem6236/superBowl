from datetime import datetime

from sqlalchemy import inspect

from .. import db  # from __init__.py

# ----------------------------------------------- #


# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Article(db.Model):
    # Auto Generated Fields:
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    created = db.Column(
        db.DateTime(timezone=True), default=datetime.now
    )  # The Date of the Instance Creation => Created one Time when Instantiation

    # Articles:
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.String, nullable=True, unique=True)
    image = db.Column(db.String, nullable=True)
    publishedAt = db.Column(db.DateTime(timezone=True), nullable=True)
    source = db.Column(db.String, nullable=True)


    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
