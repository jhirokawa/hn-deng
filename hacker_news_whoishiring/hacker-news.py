import json
import requests
import re


def get_hiring_posts(months_back: int = 1) -> list:
    """Basic API call to pull posts"""
    # Get all stories by user 'whoishiring' (official HN hiring threads account)
    user_items = requests.get(
        "https://hacker-news.firebaseio.com/v0/user/whoishiring/submitted.json"
    ).json()

    hiring_posts = []
    for item_id in user_items[:months_back]:  # Check recent submissions
        story = requests.get(f"https://hn.algolia.com/api/v1/items/{item_id}").json()

        hiring_posts.append(story["children"])

    return hiring_posts


def basic_regex_filter(posts: list, pattern: str = r".*data engineer.*") -> list:
    """Filter posts based on simple regex of top level text"""
    return [post for post in posts if re.search(pattern, post["text"])]


if __name__ == "__main__":
    for monthly_postings in get_hiring_posts():
        print(json.dumps(basic_regex_filter(monthly_postings)))
