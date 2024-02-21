# Maximum Average Subarray of size k

# import math

# k = 4
# nums = [1, 12, -5, -6, 50, 3]
# maxi = 0
# total = 0

# for i in range(0, len(nums)-3):
#     total = nums[i]
#     for j in range(1, 4):
#         total += nums[i+j]
#     if maxi == 0:
#         maxi = total/k
#     elif maxi < total/k:
#         maxi = total/k
# print(maxi)

def maxavg(nums, k):
    """
    >>> maxavg([2,2,2],3)
    2.0

    >>> maxavg([2,2,2,2,2,2,2,2,2,2],3)
    2.0

    >>> maxavg([1,2,1,2,1,2,1,2], 2)
    1.5

    >>> maxavg([1,2,3,4,5,4,3,2,1], 4)
    4.0

    >>> maxavg([4,4,4,1,1,1,7,7,7], 3)
    7.0

    >>> maxavg([3,9,3,5,7], 0)
    Traceback (most recent call last):
    ...
    Exception: Enter a valid k
    """
    maxi = 0
    total = 0

    if k == 0:
        raise Exception('Enter a valid k')

    if len(nums) <= k:
        return sum(nums)/k
   
    for i in range(0, len(nums)-(k-1)):
        total = nums[i]
        for j in range(1, k):
            total += nums[i+j]
        if maxi == 0:
            maxi = total/k
        elif maxi < total/k:
            maxi = total/k
    return maxi

# print(maxavg([4,4,4,1,1,1,7,7,7], 3))
