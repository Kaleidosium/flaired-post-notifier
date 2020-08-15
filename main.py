from notify_run import Notify
import config
import praw

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)


def send_link_notification(link):
    notify.send("New Flaired Post!", link)


def get_post_with_flair_from_subreddit(subreddit, flair):
    _subreddit = reddit.subreddit(subreddit)

    for submission in _subreddit.stream.submissions(skip_existing=True):
        _flair = submission.link_flair_text

        if _flair == flair:
            send_link_notification(submission.url)


if __name__ == "__main__":
    notify = Notify(endpoint=config.endpoint)

    get_post_with_flair_from_subreddit("python", "Beginner Showcase")
