import requests
import os
from flask import jsonify
from .models import Article
from sqlalchemy.exc import IntegrityError
from .. import db

def fetch_and_save_articles():
    apikey = os.getenv("GNEWS")

    url = f"https://gnews.io/api/v4/search?q=superbowl&lang=en&country=us&max=10&apikey={apikey}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch articles: {response.status_code}")
        return jsonify("Failed to fetch articles"), response.status_code
    data = response.json()
    articles = data.get("articles", [])

    print("Fetching articles and saving to db...")
    for article in articles:
        title = article.get("title")
        description = article.get("description")
        content = article.get("content")
        url = article.get("url")
        image = article.get("image")
        publishedAt = article.get("publishedAt")
        source = article.get("source", {}).get("name")

        # Check if an article with the same URL already exists
        existing_article = Article.query.filter_by(url=url).first()
        if existing_article:
            print(f"Article with URL {url} already exists. Skipping...")
            continue

        new_article = Article(
            title=title,
            description=description,
            content=content,
            url=url,
            image=image,
            publishedAt=publishedAt,
            source=source
        )

        try:
            db.session.add(new_article)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(f"IntegrityError: Article with URL {url} already exists.")
        return jsonify("Saved to db")