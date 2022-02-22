import requests
from secrets import *
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': REDDIT_USERNAME, 'password': REDDIT_PASSWORD}
auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
r = requests.post(base_url + 'api/v1/acces_token',
	data=data,
	headers={'user-agent': 'APP_NAME by REDDIT_USERNAME'},
	auth=auth)
d = r.json()
print(d)