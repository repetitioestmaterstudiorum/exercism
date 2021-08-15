import re

def abbreviate(words): 
    return ''.join(word[0] for word in re.findall(r"[a-z']+", words, flags=re.IGNORECASE)).upper()
    
    # alternative solution
    # return ''.join(re.findall(r"\b(?:\w)", words.replace("_", "").replace("'", ""))).upper()
   
print(abbreviate("Portable network _graphics_ what's up"))
