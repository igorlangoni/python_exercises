def sorting_in_place(nums):
    # bring all the 0 to the left side, keep non-zeroes order, in-place
    # space O(1)
    # time O(n)

    """
    >>> sorting_in_place([1, 0])
    [0, 1]

    >>> sorting_in_place([1, 2, 0])
    [0, 1, 2]

    >>> sorting_in_place([2, 1, 0])
    [0, 2, 1]

    >>> sorting_in_place([1, 0, 1, 0, 2, 0])
    [0, 0, 0, 1, 1, 2]

    >>> sorting_in_place([3, 2, 5, 0, 0, 0])
    [0, 0, 0, 3, 2, 5]

    >>> sorting_in_place([1, 2, 3])
    [1, 2, 3]

    >>> sorting_in_place([0, 1, 2])
    [0, 1, 2]

    >>> sorting_in_place([2, 3, 4, 1, 0, 4, 5, 6, 7, 0, 0, 1, 2, 3, 0])
    [0, 0, 0, 0, 2, 3, 4, 1, 4, 5, 6, 7, 1, 2, 3]
    """

    fzero = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            j = i-1
            while j >= fzero:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i -= 1
            fzero += 1
    print(nums)

# print(sorting_in_place([2, 1, 0]))

def sorting_in_place_right_side(nums):
    # bring all the 0 to the right side, keep non-zeroes order, in-place
    # space O(1)
    # time O(n)
    
    """
    # >>> sorting_in_place_right_side([0])

    >>> sorting_in_place_right_side([0,1])
    [1, 0]

    >>> sorting_in_place_right_side([1, 0])
    [1, 0]

    >>> sorting_in_place_right_side([1, 0, 1])
    [1, 1, 0]

    >>> sorting_in_place_right_side([2, 0, 1, 0])
    [2, 1, 0, 0]

    >>> sorting_in_place_right_side([2, 0, 1, 3, 4, 5, 6, 0, 2, 2, 0, 0, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 5, 0, 0, 0])
    [2, 1, 3, 4, 5, 6, 2, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    prev = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[prev], nums[i] = nums[i], nums[prev]
            prev += 1
    print(nums)
    

print(sorting_in_place_right_side([2, 0, 1, 3, 4, 5, 6, 0, 2, 2, 0, 0, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 5, 0, 0, 0]))

