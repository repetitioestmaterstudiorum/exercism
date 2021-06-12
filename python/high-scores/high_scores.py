def latest(scores):
    return scores[-1]

def personal_best(scores):
    # return sorted(scores, reverse=True)[0]
    best = float('-inf')
    for s in scores:
        if s > best:
            best = s
    return best if best != float('-inf') else []

def personal_top_three(scores):
    # return sorted(scores, reverse=True)[:3]
    high_scores = {1: float('-inf'), 2: float('-inf'), 3: float('-inf')}
    for s in scores:
        if s > high_scores[1]:
            high_scores[3] = high_scores[2]
            high_scores[2] = high_scores[1]
            high_scores[1] = s
        elif s > high_scores[2]:
            high_scores[3] = high_scores[2]
            high_scores[2] = s
        elif s > high_scores[3]:
            high_scores[3] = s
    return list(score for score in high_scores.values() if score != float('-inf')) or []

# dev tests
l = [1, 2, 0, 4, 5, 2, 3, 4]
assert(latest(l) == 4)
assert(personal_best(l) == 5)
assert(personal_top_three(l) == [5, 4, 4])

# list notes and dev tests
# l = [1,2,3] 
# print(l)
# l[len(l):] = [4]
# print(l)
# l.append(5)
# print(l)
# l.extend([2, 3, 4])
# print(l)
# l.insert(1, 99)
# print(l)
# l.remove(99)
# print(l[:3]) # last 3 positions
# print(l[3:]) # all positions after 3
# print(l[-1]) # position length -1
# print()
# print('final list', l)
# print('...')
# print(latest(l))
# print(personal_best(l))
# print(personal_top_three(l))
# print('...')
