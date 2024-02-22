"""
In this one you are given an array representing versions of a software.
You are also given an API Bool that returns False if a version is good and True if it is bad.
From the first bad version on, every version will also be bad.
You have to find the first bad version and return it.
e.g:
    [1, 2, 3, 4, 5], 4
    isBadVersion(3) -> False
    isBadVersion(5) -> True
    isBadVersion(4) -> True
    returns 4
3 was still a good version.
5 was already bad.
We check 4 to be sure where it started. Since 4 is bad, 4 is the first bad one, we return 4.
"""

from random import randint 

def checks_versions(versions):
    first_bad = randint(1, len(versions)-1)
    return first_bad
    

def isBadVersion(versions, version, fb):
    if versions.index(version)+1 < fb:
        return True
    return False


def finds_bad_version(versions):
    fb = checks_versions(versions)
    fbv = versions[fb-1]
    print(f"first badv: {fbv}")
    for i in range(len(versions)):
        # print(f"version {versions[i]}: {isBadVersion(versions, versions[i], fb)}")
        if not isBadVersion(versions, versions[i], fb):
        #     print(f"versions: {versions}")
        #     print(f"first bad: {fb}")
            return i+1

def finds_bad_version_with_binary_search(versions):
    # fb = checks_versions(versions)
    fb = 5
    # print(fb)
    fbv = versions[fb-1]
    # print(f"first badv: {fbv}")
    left = 0
    right = len(versions)-1
    mid = (len(versions))//2
    # print(versions)
    while left < right:
        mid = (len(versions[left:right])//2)
        # print(f"extract: {versions[left:right+1]}")
        # print(f"mid:{mid}")
        if isBadVersion(versions, versions[mid], fb) == False:
            right = mid
        else:
            left +=1
    res = left+1
    return versions, res, fbv
        
    



print(finds_bad_version_with_binary_search(['v1','v2','v3', 3, "v4",'v5']))