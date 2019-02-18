import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl
import pprint

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# file = "twitter_info.json"


def twitter():
    print('')
    acct = input('Enter Twitter Account:')

    if (len(acct) < 1):
        return None
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    headers = dict(connection.getheaders())
    return js


def json_handle(info):
    js = twitter()
    for u in js['users']:
        print(u['screen_name'])
        if info == "followers":
            print("Number of followers: ", u['followers_count'])
        elif info == "url":
            if 'url' not in u:
                print("No url found")
            else:
                print(u['url'])
        elif info == 'id':
            print("Profile's id:", u['id'])
        elif info == "all":
            print(u['url'])
            print("Profile's id:", u['id'])
            print("Number of followers: ", u['followers_count'])


if __name__ == "__main__":
    print("If you want to get information on users' followers amount, input 'followers',\
if you want to know about url, input 'url', if about id, input 'id' and if you want to get ALL the info, input 'all'")
    info = str(input())
    json_handle(info)
