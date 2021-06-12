import string

def is_pangram(sentence):
    if not isinstance(sentence, str):
        raise TypeError('argument "sentence" must be of type "str"')

    return all(letter in sentence.lower() for letter in string.ascii_lowercase)

    # stillPangram = True

    # for letter in 'abcdefghijklmnopqrstuvwxyz':
    #     if not letter in sentence.lower():
    #         stillPangram = False

    # return stillPangram
