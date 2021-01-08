#!/usr/bin/python

def permute(s):

    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for index, letter in enumerate(s):

            for perm in permute(s[:index] + s[index + 1:]):

                out += [letter + perm]
    
    return out

no_dups = set(permute('tryittime '))
print(no_dups)

