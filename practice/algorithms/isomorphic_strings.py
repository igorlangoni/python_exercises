def is_isomorphic(num):
    """
    >>> is_isomorphic(19)
    True
    
    >>> is_isomorphic(0)
    False

    >>> is_isomorphic(1)
    True

    >>> is_isomorphic(2)
    False

    >>> is_isomorphic(4)
    False
    """
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum([pow(int(n)%10, 2) for n in str(num)])
        if num == 1:
            return True
    return False

# print(is_isomorphic(6))
