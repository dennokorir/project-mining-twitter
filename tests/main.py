import user_tweets_search as twttr
import threading


running = True
command = ''
search = ''


def user_exit_input():
    command = input("Press Q to quit and any other key to continue \t")
    if command.lower() == 'q':
        #print("Exiting...")
        return True

def search_query():

    search_string = input("Who are we stalking? \t Q for exit \t")
    search = 'search_string'
    print("Searching for ",search_string)
    result = twttr.search(search_string)
    return result

def display(s):
    print("Showing search results")
    twttr.display(s)

#onstart
while running:
    search = search_query()
    display(search)

    if user_exit_input():#Always provide an option to quit
        print('Exiting...')
        break



