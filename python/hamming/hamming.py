def distance(strand_a, strand_b):
    if not isinstance(strand_a, str) or not isinstance(strand_b, str):
        raise TypeError('Strands to compare must be of type string!')
    elif len(strand_a) != len(strand_b):
        raise ValueError('Strands to compare must be of equal length!')

    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))

# dev test
# print(distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))

# initial return line
# return sum(True for x in range(len(strand_a)) if strand_a[x] != strand_b[x])