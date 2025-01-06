import requests
from datetime import datetime


def get_hiring_posts(months_back=3):
    # Get all stories by user 'whoishiring' (official HN hiring threads account)
    user_items = requests.get(
        "https://hacker-news.firebaseio.com/v0/user/whoishiring/submitted.json"
    ).json()

    hiring_posts = []
    for item_id in user_items[:30]:  # Check recent submissions
        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        if "who's hiring" in story.get("title", "").lower():
            hiring_posts.append(story)

    return hiring_posts
