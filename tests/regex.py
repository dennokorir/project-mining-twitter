#regex test
import re
patterns = ["#","@"]
random_words = ["#uberwars",'some','other','random','@words']
#for word in random_words:
#    for item in pattern:
#        if re.search(item,word):
#            print(word)
print([word for pattern in patterns
    for word in random_words if re.search(word,pattern) == None])
