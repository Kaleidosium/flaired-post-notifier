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



def get_multireddit_stream(subreddit_dict):
    return reddit.subreddit("+".join(subreddit_dict)).stream.submissions(
        skip_existing=True
    )


def filter_flairs(submission_gen, subreddit_dict):
    for submission in submission_gen:
        subreddit = submission.subreddit.display_name
        if submission.link_flair_text in subreddit_dict[subreddit]:
            yield submission


def send_notifications(subreddit_dict):
    multireddit_stream = get_multireddit_stream(subreddit_dict)
    for submission in filter_flairs(multireddit_stream, subreddit_dict):
        notify.send(
            f"New Flaired Post from r/{submission.subreddit.display_name}!",
            submission.url,
        )


if __name__ == "__main__":
    send_notifications(config.subreddit_dict)
