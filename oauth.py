import twitter

def authenticate():
    CONSUMER_KEY = 'Xsetvxfd73PzqPgNgSP7loLt2'
    CONSUMER_SECRET = 'XDiPEMrL3aPfNY64YFdtmekYF4HA6mSU4T4Ea664bCzgK1XSUy'
    OAUTH_TOKEN = '521109090-kJnpb0ZDTaptIustC5Fb5WUgt2dL4wT6qkLACc3I'
    OAUTH_TOKEN_SECRET = 'KUnwM4jeQ6vyTuAK3Xsf9rGV5BJjaMoOq7S1u29OvOBzz'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,
        CONSUMER_KEY,CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return  twitter_api
