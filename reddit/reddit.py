import requests
url = "https://www.reddit.com/r/me_irl/.json"
json_post = requests.get(url,headers={"user-agent":"youtube video"}).json()
json_data = json_post["data"]
json_children = json_data["children"]
for post in json_children:
    post_data = post["data"]
    url = post_data["url"]
    title = post_data["title"]
    text = post_data["selftext"]
    thumb = post_data["thumbnail"]
    print(thumb)

