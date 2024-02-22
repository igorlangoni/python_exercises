from timer import compare, runtimer
from random import randint


def find_judge(n, arr):

    """
    The idea here is that there are n people (each person has their own int id) in this town.
    Everybody trusts the judge, and the judge trusts no one.
    For each person you are given a list with their id and person they trust.
    If someone trusts more than one person, you have multiple lists with the same id and differente 'trustees'.
    E.g. N = 3, [ [1, 2], [1, 3], [3, 2]]
        There a N=3 people in town.
        Person 1 trusts persons 2 and 3.
        Person 2 trusts no one.
        Person 3 trusts person 2.
        Thus, 2 is the judge --> Trusts no one and is trusted by all
    
    Given N and the list of 'trustees' return the judge's id.

    >>> find_judge(2, [[1,2]])
    2

    >>> find_judge(1, [])
    1

    >>> find_judge(3, [[2, 1], [3, 1]])
    1

    >>> find_judge(5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 5]])
    5

    >>> find_judge(5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 3], [2, 4], [2, 5], [5, 1], [5, 2], [5, 4], [5, 3], [4, 1], [4, 2], [4, 3], [4, 5]])
    3
    """
    if arr == [] and n == 1:
        return 1
    else:
        poss_id = sorted(set(range(1, n+1)))
        for person in arr:
            if person[0] in poss_id:
                poss_id.remove(person[0])
        return poss_id[0]

# find_judge(3, [[2, 1], [3,1]])

def find_judge_alt(n, arr):
    """
    >>> find_judge_alt(2, [[1,2]])
    2

    >>> find_judge_alt(1, [])
    1

    >>> find_judge_alt(3, [[2, 1], [3, 1]])
    1

    >>> find_judge_alt(5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 5]])
    5

    >>> find_judge_alt(5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 3], [2, 4], [2, 5], [5, 1], [5, 2], [5, 4], [5, 3], [4, 1], [4, 2], [4, 3], [4, 5]])
    3
    """

    trust_count = [0] * (n+1)
    for person1, person2 in arr:
        trust_count[person1] -= 1
        trust_count[person2] += 1
    for i in range(1, n+1):
        if trust_count[i] == n-1:
            return i
    return -1

# creates random n, judge and trusting relationships

n = randint(500, 550)
# print(f"n: {n}")
j = randint(1, n)
# print(f"j: {j}")
args = []
pop = set(range(n))
pop.remove(j)
# print(f"pop: {len(pop)}")
acc = 0
for id in pop:
    x = randint(1, len(pop)+1)
    acc += x
    while x > 0:
        if [id, j] not in args:
            args.append([id, j])
        t = randint(1, max(pop))
        if id != t and [id, t] not in args:
            args.append([id, t])
        x -= 1
# print(f"args: {args}")
# print(len(args))
# print(len(args[0]))
print(f'{n}... args ready')
print(len(args))
print(acc/len(pop))

# find_judge_alt(n, args)
compare(runtimer(find_judge(n, args), 1000), runtimer(find_judge_alt(n, args), 1000))
