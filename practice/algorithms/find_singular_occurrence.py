from collections import Counter
import timeit

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
    

    methods = {}

    # space O(1)
    # time O(n)

    st = timeit.default_timer()
    for n in nums:
        if nums.count(n) == 1:
            ft = timeit.default_timer()
            methods['for_loop'] = (ft-st)*1000
            
    

    # space O(n)
    # time O(n)

    st = timeit.default_timer()
    single = Counter(nums).most_common(len(set(nums)))[-1][0]
    ft = timeit.default_timer()
    methods['Counter'] = (ft-st)*1000

    # space 0(n)
    # time 0(n)
    
    st = timeit.default_timer()
    acc = 0
    for n in nums:
        acc ^= n
    ft = timeit.default_timer()
    methods['xor'] = (ft-st)*1000

    # Faster_to_slowest(ms): XOR(0,001) > for_loop(0,007) > counter(1,0+)

    print(sorted(methods.items(), key=lambda v:v[1], reverse=True))

is_single([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,24,9,10,10,11,11,12,12,100,100,5000,5000])