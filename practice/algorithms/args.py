import string
from random import randint
from collections import Counter


def find_non_repeat_args():
    args = ''
    alphabet = string.ascii_letters
    answer = randint(0, 52)
    for i, letter in enumerate(alphabet):
        if i != answer:
            args += letter*(randint(2, 5))
        else:
            args += letter
    return args


args = find_non_repeat_args()
args = args
print(Counter(args))