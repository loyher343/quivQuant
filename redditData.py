import requests, json
from secrets import *

#get token
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': REDDIT_USERNAME, 'password': REDDIT_PASSWORD}
auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
r = requests.post(base_url + 'api/v1/access_token',
    data=data,
    headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
	auth=auth
)
d = r.json()
#print(d)

#api access
token = 'bearer ' + d['access_token']
api_url = 'https://oauth.reddit.com'
headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}

# #api test
# response = requests.get(api_url + '/api/v1/me', headers=headers)
# if response.status_code == 200:
#     print(response.json()['name'], response.json()['comment_karma'])

# print(r.status_code)

# payload = {'q': 'puppies', 'limit': 5, 'sort': 'relevance'}
# response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
# print(response.json())

payload = {}
response = requests.get(api_url + '/r/wallstreetbets', headers=headers, params=payload)
parse = response.json()
#['data']['children'][i]['selftext']
#print(json.dumps(parse['data']['children'], indent = 4))
posts = response.json()['data']['children']
#print(json.dumps(posts, indent = 4))

print('/////////////////////////////////////////////////////////////////////////////////////////               ')
#"link_flair_text": "DD"
list = []
for i in range(len(posts)):
    post = posts[i]['data']
    # if post['link_flair_text'] == 'DD' or 'yolo':
    #     parsedPosts = { 
    #         'title' : post['title'],
    #         'upVotes' : post['ups'],
    #         'upRation' : post['upvote_ratio'],
    #         'text' : post['selftext']
    #     }
    parsedPosts = { 
        'title' : post['title'],
        'upVotes' : post['ups'],
        'upRation' : post['upvote_ratio'],
        'text' : post['selftext']
    }
    list.append(parsedPosts)

for x in range(len(list)):
    #print(list[x],'\n =============================================== \n',list[x]['text'])
    print(list[x]['title'],'   ',list[x]['upRation'])
print(len(list))