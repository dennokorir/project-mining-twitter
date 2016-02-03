import twitter, oauth

twitter_api = oauth.authenticate()


WORLD_WOE_ID = 1
KE_WOE_ID = 23424863


world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
kenya_trends = twitter_api.trends.place(_id=KE_WOE_ID)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
kenya_trends_set = set([trend['name'] for trend in kenya_trends[0]['trends']])
common_trends = world_trends_set.intersection(kenya_trends_set)
print(common_trends)
#print(world_trends)
#print
#print(kenya_trends)
