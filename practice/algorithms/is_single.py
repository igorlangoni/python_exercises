from timer import runtimer, compare
from collections import Counter

def is_single(nums):
    """
    >>> is_single([1])
    1

    >>> is_single([1,2,2])
    1

    >>> is_single([1,2,1])
    2

    >>> is_single([4,1,2,1,2])
    4
    """

    for n in nums:
        if nums.count(n) == 1:
            return n

def is_single_with_counter(nums):
    """
    >>> is_single([1])
    1

    >>> is_single([1,2,2])
    1

    >>> is_single([1,2,1])
    2

    >>> is_single([4,1,2,1,2])
    4
    """
    single = Counter(nums).most_common(len(set(nums)))[-1][0]
    return single

def is_single_with_xor(nums):
    """
    >>> is_single([1])
    1

    >>> is_single([1,2,2])
    1

    >>> is_single([1,2,1])
    2

    >>> is_single([4,1,2,1,2])
    4
    """
    acc = 0
    for n in nums:
        acc ^= n
    return acc

arg = [5,5,3,3,1,9,9,200,200,40,3,6,7,10,7,3,6,10,40]
print(compare(runtimer(is_single(arg)), runtimer(is_single_with_counter(arg)), runtimer(is_single_with_xor(arg))))



