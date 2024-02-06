import time
import datetime
import praw
import requests
import json
import os
import dotenv

dotenv.load_dotenv()

all_events = []

orcid_id = os.environ.get("ORCID_ID")
hackernews_username = os.environ.get("HACKERNEWS_USERNAME")
github_token = os.environ.get("GITHUB_TOKEN")
github_username = os.environ.get("GITHUB_USERNAME")
reddit_client_id = os.environ.get("REDDIT_CLIENT_ID")
reddit_client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
reddit_password = os.environ.get("REDDIT_PASSWORD")
reddit_user_agent = os.environ.get("REDDIT_USER_AGENT")
reddit_username = os.environ.get("REDDIT_USERNAME")

###############################################################################

api_url = f'https://pub.orcid.org/v2.1/{orcid_id}/works'
headers = {
    'Accept': 'application/json',
}
response = requests.get(api_url, headers=headers)
data = json.loads(response.text)

for work in data['group']:
    title = work['work-summary'][0]['title']['title']['value']
    # convert unicode to HTML entities
    title = title.encode('ascii', 'xmlcharrefreplace').decode()
    publication_datetime = work['work-summary'][0]['publication-date']
    year = publication_datetime['year']['value']
    month = publication_datetime['month']['value']
    try:
        day = publication_datetime['day']['value']
        publication_date = f"{year}-{month}-{day}"
        publication_datetime = datetime.datetime.strptime(publication_date, '%Y-%m-%d')
    except TypeError:
        publication_date = f"{year}-{month}"
        publication_datetime = datetime.datetime.strptime(publication_date, '%Y-%m')
    url = work['work-summary'][0]['path']
    url = f'https://orcid.org/{url}'

    print(f'Title: {title}, Publication Date: {publication_datetime}, URL: {url}')

    event = {
        'text': title,
        'time': publication_datetime,
        'url': url,
        'source': 'orcid'
    }

    if event not in all_events:
        all_events.append(event)

###############################################################################

user_url = f"https://hacker-news.firebaseio.com/v0/user/{hackernews_username}.json"
user_detail = requests.get(user_url).json()

item_ids = user_detail.get('submitted', [])

for item_id in item_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    item_detail = requests.get(item_url).json()

    item_type = item_detail.get('type')
    if item_type in ['story', 'comment']:
        item_text = item_detail.get('text')
        item_time = item_detail.get('time')
        item_time = datetime.datetime.fromtimestamp(item_time)
        item_link = f"https://news.ycombinator.com/item?id={item_id}"

        print(f"Text: {item_text}")
        print(f"Time: {item_time}")
        print(f"URL: {item_link}")
        print("\n")
        time.sleep(0.1)  # to prevent rate limiting

        event = {
            'text': item_text,
            'time': item_time,
            'url': item_link,
            'source': 'hackernews'
        }

        if event not in all_events:
            all_events.append(event)

###############################################################################

headers = {'Authorization': 'token ' + github_token}

repos = requests.get(
    f'https://api.github.com/users/{github_username}/repos',
    headers=headers
)

for repo in repos.json():
    repo_name = repo['name']
    if repo_name == 'kwertyops.github.io':
        continue

    commits = requests.get(
        f'https://api.github.com/repos/{github_username}/{repo_name}/commits',
        headers=headers
    )

    for commit in commits.json():
        commit_datetime = datetime.datetime.strptime(
            commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
        print(f"Repository: {repo_name}")
        print(f"Commit: {commit['commit']['message']}")
        print(f"Date: {commit_datetime}")
        print(f"URL: {commit['html_url']}")
        print("\n")

        event = {
            'text': commit['commit']['message'],
            'time': commit_datetime,
            'url': commit['html_url'],
            'source': 'github'
        }

        if event not in all_events:
            all_events.append(event)

###############################################################################

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    password=reddit_password,
    user_agent=reddit_user_agent,
    username=reddit_username
)

user = reddit.redditor(reddit_username)

for submission in user.submissions.new():
    print(f"Title: {submission.title}")
    print(f"Description: {submission.selftext}")
    print(f"Thumbnail: {submission.thumbnail}")
    print(
        f"Date and Time: {datetime.datetime.fromtimestamp(submission.created_utc)}")
    print(f"URL: {submission.url}")

for comment in user.comments.new():
    print(f"Comment: {comment.body}")
    print(f"Date and Time: {datetime.datetime.fromtimestamp(comment.created_utc)}")
    print(f"URL: https://reddit.com{comment.permalink}")

    event = {
        'text': comment.body,
        'time': datetime.datetime.fromtimestamp(comment.created_utc),
        'url': f"https://reddit.com{comment.permalink}",
        'source': 'reddit'
    }

    if event not in all_events:
        all_events.append(event)

###############################################################################

all_events.sort(key=lambda x: x['time'], reverse=True)

for event in all_events:
    date = str(event['time']).split(' ')[0]
    clock = str(event['time']).split(' ')[1].replace(':', '-')
    filename = f"_posts/{date}-{clock}-{event['source']}.md"
    if 'text' in event and event['text'] is not None:
        event['text'] = event['text'].replace('<p>', '\n\n')
    with open(filename, 'w') as f:
        f.write(
            f'''---
layout: post
title: {clock}-{event['source']}
date: {event['time']}
permalink: {event['url']}
---

###### {event['time']} [{event['url']}]
{event['text']}
'''
        )
