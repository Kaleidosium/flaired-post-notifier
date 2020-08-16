from notify_run import Notify
from praw import Reddit
import config

reddit = Reddit(
    client_id=config.reddit_client_id,
    client_secret=config.reddit_client_secret,
    user_agent=config.reddit_user_agent,
    username=config.reddit_username,
    password=config.reddit_password,
)
notify = Notify(endpoint=config.notify_endpoint)


def send_link_notification(subreddit, link):
    notify.send(f"New Flaired Post from r/{subreddit}!", link)


def get_post_with_flair_from_subreddit(subreddit, flair):
    _subreddit = reddit.subreddit(subreddit)

    for submission in _subreddit.stream.submissions(skip_existing=True):
        _flair = submission.link_flair_text

        if _flair == flair:
            send_link_notification(subreddit, submission.url)


if __name__ == "__main__":
    get_post_with_flair_from_subreddit("python", "Beginner Showcase")
