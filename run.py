
import time, sys, os, json,oauth, urllib, requests
from collections import Counter
from prettytable import PrettyTable


#uses a fetch, store, read, display cycle

def search(query):
    print('Searching...'),
    sys.stdout.flush()
    twitter_api = oauth.authenticate()#twitter.Twitter(auth=auth)

    q = query

    count = 1000

    search_results = twitter_api.search.tweets(q = q , count = count, lang = 'en', result_type = 'recent', screen_name = query)

    #for item in search_results:
    statuses = search_results['statuses']

    status_texts = [status['text'] for status in statuses]#.encode('utf-8')

    summary = [status.replace("\"","") for status in status_texts]

    summary = "".join(status_texts).split(" ")

    summary = clean(summary)#remove stop words

    if summary:
        data_file = open('data.json', 'w')
        json.dump(summary,data_file)
        data_file.close()

    display()

def clean(param):#param should be a list
    print('Cleaning...'),
    sys.stdout.flush()
    stop_words = open('stop_words_lib.txt','r').readlines()
    stop_words = "".join(stop_words).split(",")
    param = [word for word in param if word.lower() not in stop_words]
    return param

def display(limit = 10):#param holds a data in form of a list
    print('Reading...'),
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.flush()
    data_file = open('data.json', 'r')
    data = json.load(data_file)
    data_file.close()
    data = [word.encode('utf-8') for word in data]

    #remove file after display finishes
    os.remove('data.json')


    pt = PrettyTable(field_names = ["Status Text", 'Count'])
    c = Counter(data)


    table = [pt.add_row(row) for row in c.most_common()[:limit]]
    #pt.add_column("Rank",[i+1 for i in range(len(table))])

    pt.align["Status Text"], pt.align['Count'] = 'l', 'r'
    print(pt)

    if input("Get sentiments? Y to continue and anything else to exit \t").lower() == 'y':
        print('Catching feelings...'),
        sys.stdout.flush()

        from alchemyapi import AlchemyAPI
        alchemyapi = AlchemyAPI()
        Text = "".join([word.decode() for word in data])
        try:
            response = alchemyapi.sentiment("text",Text)#
            print("Sentiment: ", response["docSentiment"]["type"])
        except:
            print("No result to analyse")


def user_exit_input():
    command = input("Press Q to quit and any other key to continue \t")
    if command.lower() == 'q':

        return True

def search_query():
    search_string = ''
    while len(search_string)<=0:
        search_string = input("Who are we stalking? \t Q for exit \t")
    search(search_string)


#onstart
while True:

    search_query()


    if user_exit_input():#Always provide an option to quit
        print('Exiting...')
        break


