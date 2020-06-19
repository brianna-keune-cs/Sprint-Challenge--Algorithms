'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0
    # if first two letters are th, return 1, continue at index 2
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    # if first two letters are not th, return 0 and continue at next letter
    return count_th(word[1:])

'''
So I've already solved this iteratively:
I know I need to check each index compared to it's next index

if i am given 'A'
    i know it cannot be 'th' because there's not a second character

so if I have just 'th' given
if word[0] + word [1] == 'th'
    return 1

    how do I recursively do that?

if ^ doesn't match
return count_th(word(word[index_count + 1:]))

'''