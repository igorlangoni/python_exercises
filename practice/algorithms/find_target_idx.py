from timer import compare, runtimer
from math import floor
from random import random, randint


def find_target_idx(nums, k):
    """
    >>> find_target_idx([1], 1)
    0

    >>> find_target_idx([0, 1], 1)
    1

    >>> find_target_idx([0, 1, 2, 3, 4, 10, 11, 20], 11)
    6

    >>> find_target_idx([0], 1)
    1

    >>> find_target_idx([0, 1], 2)
    2

    >>> find_target_idx([0, 2], 1)
    1

    >>> find_target_idx([1, 2], 0)
    0

    >>> find_target_idx([10], 3)
    0

    >>> find_target_idx([5, 9, 12, 16, 20, 21], 10)
    2
    """
    if k in nums:
        return nums.index(k)
    else:
        i = 0
        while i < k and i < len(nums)-1:
            if nums[i] < k:
                if nums[i + 1] > k:
                    nums.insert(i+1, k)
                i += 1
            else:
                i += 1
    if k < nums[0]:
        nums.insert(0, k)
    nums.append(k)
    return nums.index(k)

def find_target_idx_with_set(nums, k):
    """
    >>> find_target_idx_with_set([1], 1)
    0

    >>> find_target_idx_with_set([0, 1], 1)
    1

    >>> find_target_idx_with_set([0, 1, 2, 3, 4, 10, 11, 20], 11)
    6

    >>> find_target_idx_with_set([0], 1)
    1

    >>> find_target_idx_with_set([0, 1], 2)
    2

    >>> find_target_idx_with_set([0, 2], 1)
    1

    >>> find_target_idx_with_set([1, 2], 0)
    0

    >>> find_target_idx_with_set([10], 3)
    0

    >>> find_target_idx_with_set([5, 9, 12, 16, 20, 21], 10)
    2
    """
    nums = set(nums)
    nums.add(k)
    nums = sorted(list(nums))
    return nums.index(k)

def find_target_idx_with_binary_search(nums, k):
    """
    >>> find_target_idx_with_binary_search([1], 1)
    0

    >>> find_target_idx_with_binary_search([0, 1], 1)
    1

    >>> find_target_idx_with_binary_search([0, 1, 2, 3, 4, 10, 11, 20], 11)
    6

    >>> find_target_idx_with_binary_search([0], 1)
    1

    >>> find_target_idx_with_binary_search([0, 1], 2)
    2

    >>> find_target_idx_with_binary_search([0, 2], 1)
    1

    >>> find_target_idx_with_binary_search([1, 2], 0)
    0

    >>> find_target_idx_with_binary_search([10], 3)
    0

    >>> find_target_idx_with_binary_search([5, 9, 12, 16, 20, 21], 10)
    2
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = floor((left+right)/2)
        if nums[mid] == k:
            return mid
        elif k < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


# playing with generating multiple test cases and arguments

args = []
k = 33
start = 0
while len(args) < randint(100000, 1000000):
    args.append(randint(start, start+randint(5,1000)))
    start = args[-1]
k = randint(0, args[-1])

print(f"min: {min(args)} // max: {max(args)} // len: {len(args)} // avg: {sum(args)/len(args)}")

# args = [2, 4, 5, 6, 9, 10, 12, 20]
# k = 3

# as n grows bigger, binary search becomes (apparently, but not always) relatively faster than the others
print(compare(runtimer(find_target_idx(args, k), 1000), runtimer(find_target_idx_with_set(args, k), 1000), runtimer(find_target_idx_with_binary_search(args, k), 1000)))
