import time, sys, os, json, oauth
from collections import Counter
from prettytable import PrettyTable

#uses a fetch, store, read, display workflow

class Twitter_Metrics(object):
    def __init__(self):
        pass

    def search(self, query):
        print('>>Searching...\n'),
        sys.stdout.flush()
        twitter_api = oauth.authenticate()

        count = 100000
        try:
            search_results = twitter_api.search.tweets(q = query , count = count, lang = 'en', result_type = 'recent', screen_name = query)
            statuses = search_results['statuses']
            status_texts = [status['text'].strip() for status in statuses]
            status_texts = [status.replace("\"","") for status in status_texts]
            summary = "".join(status_texts).split(" ")
            summary = self.clean(summary)#remove stop words

            if summary:
                data_file = open('data.json', 'w')
                json.dump(summary,data_file)
                data_file.close()

            self.display(query)


        except:
            print("No response! Check your internet connection")


    def clean(self, param):
        #function to remove stop words and unnecessary data
        print('>>Cleaning...\n'),
        sys.stdout.flush()
        stop_words = open('stop_words_lib.txt','r').readlines()
        stop_words = "".join(stop_words).split(",")
        param = [word.lower() for word in param if word.lower() not in stop_words]
        param = [word for word in param if '@' not in word]
        param = [word for word in param if '#' not in word]
        return param

    def display(self, term, limit = 10):
        print('>>Reading...\n'),
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
            limit = int(input(">>How many records do you want to view? Press enter for default(10)\n\n"))
        except:
            pass
        table = [pt.add_row(row) for row in c.most_common()[:limit]]
        pt.add_column("Rank",[i+1 for i in range(len(table))])
        pt.align["Status Text"], pt.align['Count'] = 'l', 'r'
        print("\n \nShowing top %s prominent terms in search for \"%s\" \n \n" %(limit, term))
        print(pt)

        if str(input(">>Get sentiments? Y to continue and anything else to exit \t")).lower() == 'y':
            print('>>Getting general feel of results...'),
            sys.stdout.flush()

            from alchemyapi import AlchemyAPI
            sentiment_data = [key for key, value in c.most_common()][:limit]#collect top ranked list
            alchemyapi = AlchemyAPI()
            Text = "".join([word.decode() for word in sentiment_data])
            if len(Text)<=1:
                print("No text to analyse")
            else:
                try:
                    response = alchemyapi.sentiment("text",Text)
                    print("\n\n>>Sentiment: ", response["docSentiment"]["type"])
                except:
                    print("Can't test sentiments now, try later")


