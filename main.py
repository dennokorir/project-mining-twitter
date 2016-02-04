import run as twtter
def user_exit_input():
    command = input("Press Q to quit and any other key to continue \t")
    if command.lower() == 'q':

        return True

def search_query():
    search_string = ''
    while len(search_string)<=0:
        search_string = input("Who are we stalking? \t Q for exit \t")
    twtter.search(search_string)



while True:

    search_query()

    if user_exit_input():
        print('Exiting...')
        break
