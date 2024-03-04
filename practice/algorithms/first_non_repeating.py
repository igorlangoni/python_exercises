from args import args

def find_non_repeat(str1):
    """
    Given a string, return the index of the first non repeating char in it.
    If there isnt one, return -1

    >>> find_non_repeat('a')
    0
    
    >>> find_non_repeat('aba')
    1

    >>> find_non_repeat('abcddcbja')
    7
    
    >>> find_non_repeat('aabb')
    -1

    >>> find_non_repeat(args)
    169
    """
    for i, l in enumerate(str1):
        if str1.count(l) == 1:
            return i
    return -1