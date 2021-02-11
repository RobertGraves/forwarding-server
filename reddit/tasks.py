
from datetime import datetime
from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task, periodic_task, task
from .scrape import listen_subreddit_stream

@db_task()
def task_listen_subreddit_stream(subreddit):
    listen_subreddit_stream(subreddit)