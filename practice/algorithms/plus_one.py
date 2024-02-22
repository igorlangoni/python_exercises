import timeit
import time

def plus_one(nums):
    """
    >>> plus_one([1])
    [2]

    >>> plus_one([1, 4])
    [1, 5]

    >>> plus_one([2, 1, 9, 3, 3, 0])
    [2, 1, 9, 3, 3, 1]

    >>> plus_one([9])
    [1, 0]

    >>> plus_one([2, 9])
    [3, 0]

    >>> plus_one([1, 3, 9])
    [1, 4, 0]

    >>> plus_one([1, 9, 9])
    [2, 0, 0]

    >>> plus_one([9, 9])
    [1, 0, 0]

    >>> plus_one([9, 9, 9, 9, 9, 9])
    [1, 0, 0, 0, 0, 0, 0]

    >>> plus_one([8, 9, 9, 9, 9])
    [9, 0, 0, 0, 0]
    """
    if nums[-1] == 9:
        last = 1
        while nums[-last] == 9:
            nums[-last] = 0
            last += 1
            if last > len(nums):
                nums.insert(0, 1)
                return nums
        nums[-last] += 1
    else:
        nums[-1] += 1
    return nums

def plus_one_alt(digits):
    dig_len = len(digits)
    for i in reversed(range(dig_len)):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        else:
            digits[i] = 0
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits
        
st = time.perf_counter()
plus_one([9, 9])
ft = time.perf_counter()
print(f"{((ft-st)*1000):.6f} mseconds")

st = time.perf_counter()
plus_one_alt([9, 9])
ft = time.perf_counter()
print(f"{((ft-st)*1000):.6f} mseconds")