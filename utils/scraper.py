import os
from dotenv import load_dotenv
import praw

load_dotenv()

class RedditScraper:
    def __init__(self, username):
        self.username = username

        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

        self.user = self.reddit.redditor(self.username)

    def fetch_user_activity(self, limit=20):
        posts = self._get_posts(limit)
        comments = self._get_comments(limit)
        return posts, comments

    def _get_posts(self, limit):
        post_texts = []
        try:
            for submission in self.user.submissions.new(limit=limit):
                content = f"Title: {submission.title}\nText: {submission.selftext}"
                post_texts.append(content.strip())
        except Exception as e:
            print(f"Error fetching posts: {e}")
        return post_texts

    def _get_comments(self, limit):
        comment_texts = []
        try:
            for comment in self.user.comments.new(limit=limit):
                comment_texts.append(comment.body.strip())
        except Exception as e:
            print(f"Error fetching comments: {e}")
        return comment_texts
