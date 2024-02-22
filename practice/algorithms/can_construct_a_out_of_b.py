from timer import runtimer, compare
from collections import Counter

def can_construct(a, b):
    """
    >>> can_construct('a', 'a')
    True

    >>> can_construct('a', 'ba')
    True

    >>> can_construct('b', 'a')
    False

    >>> can_construct('a', 'babb')
    True

    >>> can_construct('ab', 'bccccac')
    True

    >>> can_construct('aa', 'bcaabc')
    True

    >>> can_construct('aa', 'bcabc')
    False

    >>> can_construct('aa', 'bcabccbba')
    True

    >>> can_construct('bxbaab', 'I am a beast-born x-boy!!!')
    True
    """
    c = 0
    for i, l in enumerate(a):
        if l in b:
            c += 1
            b = b[:b.index(l)] + b[b.index(l)+1:]
    if c == len(a):
        return True
    return False

def can_construct_dict(a, b):
    """
    >>> can_construct_dict('a', 'a')
    True

    >>> can_construct_dict('a', 'ba')
    True

    >>> can_construct_dict('b', 'a')
    False

    >>> can_construct_dict('a', 'babb')
    True

    >>> can_construct_dict('ab', 'bccccac')
    True

    >>> can_construct_dict('aa', 'bcaabc')
    True

    >>> can_construct_dict('aa', 'bcabc')
    False

    >>> can_construct_dict('aa', 'bcabccbba')
    True

    >>> can_construct_dict('bxbaab', 'I am a beast-born x-boy!!!')
    True
    """
    b_dict = {}
    for l in b:
        if l not in b_dict:
            b_dict[l] = 1
        else:
            b_dict[l] += 1
    
    for l in a:
        if l not in b_dict or b_dict[l] == 0:
            return False
        b_dict[l] -= 1
    return True

def can_construct_counter(a, b):
    """
    >>> can_construct_counter('a', 'a')
    True

    >>> can_construct_counter('a', 'ba')
    True

    >>> can_construct_counter('b', 'a')
    False

    >>> can_construct_counter('a', 'babb')
    True

    >>> can_construct_counter('ab', 'bccccac')
    True

    >>> can_construct_counter('aa', 'bcaabc')
    True

    >>> can_construct_counter('aa', 'bcabc')
    False

    >>> can_construct_counter('aa', 'bcabccbba')
    True

    >>> can_construct_counter('bxbaab', 'I am a beast-born x-boy!!!')
    True
    """
    count_a = Counter(a)
    count_b = Counter(b)
    if (set(count_a) & set(count_b)) != set(count_a):
        return False
    else:
        for k in set(count_a):
            if count_b[k] < count_a[k]:
                return False
    return True

# Fastest: 1.with_counter, with_dict
#          2.for_loop

# print(f"can_construct: {runtimer(can_construct, 10)}")
# print(f"can_construct_dict: {runtimer(can_construct_dict, 10)}")
# print(f"can_construct_counter: {runtimer(can_construct_counter, 10)}")

print(compare(runtimer(can_construct), runtimer(can_construct_dict), runtimer(can_construct_counter)))
