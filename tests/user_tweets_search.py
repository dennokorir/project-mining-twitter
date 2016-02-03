#tweets search
import time, sys
import json,twitter,oauth
from collections import Counter
from prettytable import PrettyTable

#uses a fetch, store, read, display cycle
status = ''

def search(query):
    status = 'fetching...'
    twitter_api = oauth.authenticate()#twitter.Twitter(auth=auth)

    q = query

    count = 100

    search_results = twitter_api.search.tweets(q = q , count = count, lang = 'en')

    #for item in search_results:
    statuses = search_results['statuses']

    status_texts = [status['text'] for status in statuses]#.encode('utf-8')

    summary = [status.replace("\"","") for status in status_texts]

    summary = "".join(summary).split(" ")


    if summary:
        data_file = open('data.json', 'w')
        json.dump(search_results,data_file)
        data_file.close()




    '''
    summary = set(summary)
    f = open("stop_words_lib.txt")
    stop_words = f.readlines()
    stop_words = [word.replace('\n','') for word in stop_words]
    stop_words = stop_words[0].split(",")
    stop_words = set(stop_words)
    summary = summary - stop_words #Basic set operation
    summary = list(summary)

    '''
    return summary


def data_read():
    status = 'reading...'
    data_file = open('data.json', 'r',0)
    json.load(search_results,data_file)
    data_file.close()
    return data_file






def display(param, limit = 10):#param holds a data in form of a list

    label = 'Status Text'
    pt = PrettyTable(field_names = [label, 'Count'])
    c = Counter(param)
    [pt.add_row(row) for row in c.most_common()[:limit]]
    pt.align[label], pt.align['Count'] = 'l', 'r'
    print(pt)


display(search('andela_kenya'))
