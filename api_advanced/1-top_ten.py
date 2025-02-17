#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python3:top_ten:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        except ValueError:
            print(None)
    else:
        print(None)

