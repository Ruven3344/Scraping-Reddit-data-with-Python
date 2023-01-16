import praw
from praw.models import MoreComments
import pandas as pd

reddit = praw.Reddit(client_id='I-vu87MMWbuDgjqWJQOANw',
                     client_secret='I4KVCO9jE7R082zKQHm7rXcLfYgKZg', user_agent='Scraping')

subreddit = reddit.subreddit("Python")

content_dict = {"Title": [], "Author": [], "URL": [], "ID": [], "Body": [], "Post": []}

# extracting posts
for post in subreddit.top("month"):
    content_dict["Title"].append(post.title)
    content_dict["Author"].append(post.author)
    content_dict["ID"].append(post.id)
    content_dict["Body"].append(post.selftext)
    content_dict["Post"].append(True)

    # extracting comments of each post
    post_url = "https://www.reddit.com" + post.permalink
    content_dict["URL"].append(post_url)
    submission = reddit.submission(url=post_url)
    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
        content_dict["Title"].append(0)
        content_dict["Author"].append(comment.author)
        content_dict["ID"].append(comment.id)
        comment_url = "https://www.reddit.com" + comment.permalink
        content_dict["URL"].append(comment_url)
        content_dict["Body"].append(comment.body)
        content_dict["Post"].append(False)

content_df = pd.DataFrame.from_dict(content_dict, orient='columns')
content_df.to_csv("Content_data.csv")

