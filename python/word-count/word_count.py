import re
from collections import Counter

def count_words(sentence):
    return Counter(re.findall(r"\w+'\w+|\w+", sentence.lower().replace('_', ' ')))

print(count_words("hey,my_spacebar_is_broken"))
print()
print(count_words("That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled. We're all scrued"))

# older iteration
# def count_words(sentence):
#     word_list = [x.lower() for x in re.findall(r"\w+'\w|\w+", sentence.replace('_', ' '))]
#     word_set = set(word_list)
#     return {word:word_list.count(word) for word in word_set}

# on Counter and regex
# re.findall(r"[a-z0-9]+(?:'[a-z]+)?", "Hi there what's up".lower()) # ['hi', 'there', "what's", 'up']
# Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", "Hi there what's up".lower())) #Counter({'hi': 1, 'there': 1, "what's": 1, 'up': 1})
# Counter([1, 2, 3, 4, 4, 4, 3, 2, 3, 3, 3]) # Counter({3: 5, 4: 3, 2: 2, 1: 1})