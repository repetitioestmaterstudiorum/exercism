import os

def recite(start_verse, end_verse):
    readme_text = open(f'{os.getcwd()}/README.md', 'r')
    lyrics = [x.rstrip('\n') for x in readme_text if x[0:6] == 'On the']
    return lyrics[start_verse-1:end_verse]
