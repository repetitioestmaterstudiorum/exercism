def is_isogram(string):
    if not isinstance(string, str):
        raise ValueError('Oh-oh, the is_isogram function only accepts strings as input!')

    casefold_alphas = [x for x in str.casefold(string) if x.isalpha()]
    return len(set(casefold_alphas)) == len(casefold_alphas)


# initial version
# from string import ascii_lowercase

# def is_isogram(string):
#     if not isinstance(string, str):
#         raise ValueError('Oh-oh, the is_isogram function only accepts strings as input!')

#     lowercase_letters = [x for x in str.lower(string) if x in ascii_lowercase]
#     return len(set(lowercase_letters)) is len(lowercase_letters)