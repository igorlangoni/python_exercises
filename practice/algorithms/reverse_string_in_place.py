def reverse_string(arr):
    #reverse arr of strings in-place
    # space O(1)
    # space O(n)

    # .reverse() would be best practice

    """
    >>> reverse_string(['b', 'a'])
    ['a', 'b']

    >>> reverse_string(['a', 'b'])
    ['b', 'a']

    >>> reverse_string(['x', 'o', 'x', 'o'])
    ['o', 'x', 'o', 'x']

    >>> reverse_string(['a', 'a', 'b'])
    ['b', 'a', 'a']

    >>> reverse_string(['a', 'i', 'b', 'o', 'h', 'p', 'h', 'o', 'b', 'i', 'a'])
    ['a', 'i', 'b', 'o', 'h', 'p', 'h', 'o', 'b', 'i', 'a']

    >>> reverse_string([])
    []

    >>> reverse_string([1, 2, 3])
    ['3', '2', '1']

    >>> reverse_string(['1', '2', '3'])
    ['3', '2', '1']

    >>> reverse_string([True, True, False, False])
    ['False', 'False', 'True', 'True']
    """
    
    start = 0
    end = len(arr)-1
    while start <= end:
        arr[start], arr[end] = str(arr[end]), str(arr[start])
        start += 1
        end -= 1

    print(arr)