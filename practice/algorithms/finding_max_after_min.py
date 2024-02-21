def biggest_diff(arr_int):
    # function to find the best time to buy and sell stock
    # best to buy is the min()
    # best to seel is the max() after the min (max().index() > min().index())

    # returns the profit as int
    """
    >>> biggest_diff([1, 5])
    4

    >>> biggest_diff([1, 5, 7])
    6

    >>> biggest_diff([5, 5, 1, 3, 5, 9])
    8

    >>> biggest_diff([5, 5, 5, 5, 5, 5])
    0

    >>> biggest_diff([9, 1, 6])
    5

    >>> biggest_diff([15, 50, 100, 4, 5, 6, 200, 20, 1, 3])
    196

    >>> biggest_diff([20, 5, 10, 3, 10, 1, 5])
    7

    >>> biggest_diff([1, 100, 2, 5, 1, 10, 2, 98])
    99

    >>> biggest_diff([1, 20, 3, 50, 5, 50, 4, 300])
    299
    """

    min_price = float('inf')
    max_profit = 0
    for price in arr_int:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
              