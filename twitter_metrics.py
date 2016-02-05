from search import Twitter_Metrics as twtter
import sys
def user_exit_input():
    command = str(input(">> Press Q to quit and any other key to continue \t"))
    if command.lower() == 'q':
        return True

def search_query():
    search_string = ''
    while len(search_string)<=0:
        search_string = str(input(">> Enter Twitter Username \t"))
    query_obj = twtter()
    query_obj.search(search_string)


def main():
    instructions = "\n\n\n twittermetrics 101 \n" + \
                        "====================\n \n" + \
                        "Use twittermetrics to: \n\n" + \
                        "1. Search for tweets by username \n" + \
                        "2. Perform word count tests for commonly used words \n" + \
                        "3. Test the sentiments of the twitter user. Enjoy! \n\n\n"

    print(instructions)
    while True:
        search_query()
        if user_exit_input():
            print('Exiting...')
            break


if __name__ == '__main__':
    main()

