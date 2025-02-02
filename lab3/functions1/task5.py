from itertools import permutations

def print(s):
    lis = permutations(s)
    for perm in lis:
        print(''.join(perm))
