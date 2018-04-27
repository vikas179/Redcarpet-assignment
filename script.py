import json
import re

data = json.load(open('merged_file.json'))
donald_count = 0
donald_text = []
users = []
user_tweet_count = dict()
for i in range(len(data)):
	text = data[i]['text']
	if re.search('donald\W*trump', text.lower()):
		donald_count+=1
		donald_text.append(text)
		users.append(text)
		user = data[i]['user_id']
		if user in user_tweet_count:
			user_tweet_count[user]+=1
		else:
			user_tweet_count[user] = 1

final_users_dict = dict(sorted(user_tweet_count.items(), key = lambda x: x[1], reverse = True))
print('Tweets about Donald Trump', (len(donald_text)/len(data))*100)
print('List of users tweeting about Donald Trump sorted based on number of tweets')
for key,value in final_users_dict.items():
	print(key)

f = open('output.txt', 'w+')
for st in donald_text:
	f.write(st+'\n')

f.close()