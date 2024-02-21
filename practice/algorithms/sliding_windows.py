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

    """
    maxi = 0
    total = 0
    if len(nums) <= k:
        return sum(nums)/k
    for i in range(0, len(nums)-(k+1)):
        total = nums[i]
        for j in range(1, k+1):
            total += nums[i+j]
        if maxi == 0:
            maxi = total/k
        elif maxi < total/k:
            maxi = total/k
    return maxi

print(maxavg([2,2,2], 3))
