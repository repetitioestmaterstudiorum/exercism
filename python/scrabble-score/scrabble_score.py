score_system = {
            "AEIOULNRST": 1,
            "DG": 2,
            "BCMP": 3,
            "FHVWY": 4,
            "K": 5,
            "JX": 8,
            "QZ": 10
        }
scoring_dict = {letter: value for letters, value in score_system.items()
             for letter in letters}

def score(word):
    return sum(scoring_dict[letter] for letter in word.upper())

print(score('cabbage'))

# first iteration (without full scoring dict in memory)
# def score(word):
#     score_dict = {'aeioulnrst': 1, 'dg':2, 'bcmp': 3, 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}
#     return sum(v for x in word.lower() for k, v in score_dict.items() if x in k)

# nice enum solution 