def count_occurrences(s1, s2):
    """
    For this one, you are given 2 strings s1 and s2.
    Return the total amount of times letters in s1 appear in s2.
    e.g:
    s1 = 'aA'
    s2 = 'aAAbbB'
    return 3

    s1 = 'aA'
    s2 = 'ZzzzZ'
    return 0

    >>> count_occurrences('a','a')
    1

    >>> count_occurrences('a', 'aa')
    2

    >>> count_occurrences('aA', 'aAb')
    2

    >>> count_occurrences('aAbB', 'BbuiopAa')
    4

    >>> count_occurrences('aA', 'aAAbbbb')
    3

    >>> count_occurrences('z', 'ZZ')
    0

    >>> count_occurrences('', 'AbcD')
    0

    >>> count_occurrences('aaaaBBBBAAAABBBBBABBBBABBABABABABABABABABABABABABABABABABABABABABABBABABAABABBABABABABABABABBAABBABABABABABABABABBABABABABABABABABABABBABA', 'AB')
    2
    """
    count = 0
    for l in s2:
        if l in set(s1):
            count += 1
    return count

