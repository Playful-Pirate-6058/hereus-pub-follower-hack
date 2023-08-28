import requests
import getpass
import json

username = input('username> ').replace('@','_at_')

for user in json.loads(requests.get('https://activitypub-redirector.vercel.app/search/mastodon.social/'+input('topic> ')).content)['results']:
	print(user['email'], end='     ')
	print(json.loads(requests.post('https://hereus.pythonanywhere.com/users/'+username+'/inbox', data={
		"@context": "https://www.w3.org/ns/activitystreams",
		"id": "http://localhost/inbox/lolfake",
		"type": "Follow",
		"actor": "https://"+user['email'].split('@')[2]+'/users/'+user['email'].split('@')[1],
		"object": {
			"id": 'https://hereus.pythonanywhere.com/users/'+username,
			"type": "Person"
		}
	}).content))