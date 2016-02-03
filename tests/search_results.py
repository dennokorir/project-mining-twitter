#Collecting search results
import time, sys
import json,twitter,oauth
from collections import Counter
from prettytable import PrettyTable




def search(query):
    twitter_api = oauth.authenticate()#twitter.Twitter(auth=auth)

    q = query

    count = 100

    search_results = twitter_api.search.tweets(q = q, result_type = 'recent', count = count, lang = 'en')

    if search_results:
        data_file = open('data.json', 'w')
        json.dump(search_results,data_file)
        data_file.close()
    return data_file

def read_data():
    data = open('data.json','r')
    search_results = json.load(data)
    data.close()
    for item in search_results:
        statuses = search_results['statuses']

        status_texts = [status['text'].encode('utf-8') for status in statuses]

        screen_names = [user_mention['screen_name']
                        for status in statuses
                            for user_mention in status['entities']['user_mentions']]

        hashtags = [hashtag['text']
                    for status in statuses
                        for hashtag in status['entities']['hashtags']]
        result = [status_texts,screen_names,hashtags]
        return result



def my_print(s):

    for label, data in (('status texts',s[0]),
                        ('screen_names',s[1]),
                        ('hashtags',s[2])):
        pt = PrettyTable(field_names = [label, 'Count'])
        c = Counter(data)
        [pt.add_row(kv) for kv in c.most_common()[:10]]
        pt.align[label], pt.align['Count'] = 'l', 'r'

        print(pt)

search('andela')
my_print(read_data())




