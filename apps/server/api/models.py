from datetime import datetime

from sqlalchemy import inspect
from sqlalchemy.orm import validates

from .. import db  # from __init__.py

# ----------------------------------------------- #


# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Article(db.Model):
    # Auto Generated Fields:
    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created = db.Column(
        db.DateTime(timezone=True), default=datetime.now
    )  # The Date of the Instance Creation => Created one Time when Instantiation
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )  # The Date of the Instance Update => Changed with Every Update

    # Input by User Fields:
    title = db.Column(db.String(100), nullable=False, unique=True)
    source = db.Column(db.String(100), nullable=False)
    url = db.Column(db.URL, nullable=False)
    summary = db.Column(db.String(1000), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Validated Fields:
    @validates("title")
    def validate_title(self, key, title):
        assert len(title) > 0, "Title is required"

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
