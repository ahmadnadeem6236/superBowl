import os
from apscheduler.schedulers.background import BackgroundScheduler

# App Initialization
from . import create_app  # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))

# ----------------------------------------------- #


# Hello World!
@app.route("/")
def hello():
    return "Hello World🙋"


# Applications Routes
from .api import urls

# ----------------------------------------------- #
# from .api.utils import fetch_and_save_articles
#
# def start_scheduler():
#     scheduler = BackgroundScheduler()
#
#     def job_wrapper():
#         with app.app_context():
#             fetch_and_save_articles()
#
#     scheduler.add_job(job_wrapper, 'interval', seconds=10)
#     scheduler.start()
#
# with app.app_context():
#     start_scheduler()

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()
