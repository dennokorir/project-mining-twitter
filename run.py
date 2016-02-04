import time, sys, os, json,oauth, urllib, requests
from collections import Counter
from prettytable import PrettyTable


#uses a fetch, store, read, display cycle

def search(query):
    print('Searching...'),
    sys.stdout.flush()
    twitter_api = oauth.authenticate()

    count = 1000
    try:
        search_results = twitter_api.search.tweets(q = query , count = count, lang = 'en', result_type = 'recent', screen_name = query)
    except:
        print("No response! Check your internet connection")

    statuses = search_results['statuses']
    status_texts = [status['text'].strip() for status in statuses]
    summary = [status.replace("\"","") for status in status_texts]
    summary = "".join(status_texts).split(" ")
    summary = clean(summary)#remove stop words

    if summary:
        data_file = open('data.json', 'w')
        json.dump(summary,data_file)
        data_file.close()

    display(query)

def clean(param):
    #function to remove stop words and unnecessary data
    print('Cleaning...'),
    sys.stdout.flush()
    stop_words = open('stop_words_lib.txt','r').readlines()
    stop_words = "".join(stop_words).split(",")
    param = [word for word in param if word.lower() not in stop_words]
    param = [word for word in param if '@' not in word]
    return param

def display(term,limit = 10):
    print('Reading...'),
    sys.stdout.flush()
    time.sleep(1)
    data_file = open('data.json', 'r')
    data = json.load(data_file)
    data_file.close()
    data = [word.strip().encode('utf-8') for word in data]

    #remove file after retrieving data
    os.remove('data.json')

    pt = PrettyTable(field_names = ["Status Text", 'Count'])
    c = Counter(data)

    try:
        limit = int(input("How many records do you want to view? Press enter for default(10)"))
    except:
        pass
    table = [pt.add_row(row) for row in c.most_common()[:limit]]
    pt.add_column("Rank",[i+1 for i in range(len(table))])
    pt.align["Status Text"], pt.align['Count'] = 'l', 'r'
    print("\n \nShowing top %s prominent terms in search for %s \n \n" %(limit, term))
    print(pt)

    if input("Get sentiments? Y to continue and anything else to exit \t").lower() == 'y':
        print('Catching feelings...'),
        sys.stdout.flush()

        from alchemyapi import AlchemyAPI
        sentiment_data = [key for key, value in c.most_common()][:limit]#collect top ranked list
        alchemyapi = AlchemyAPI()
        Text = "".join([word.decode() for word in sentiment_data])
        try:
            response = alchemyapi.sentiment("text",Text)
            print("Sentiment: ", response["docSentiment"]["type"])
        except:
            print("No data to analyse")


