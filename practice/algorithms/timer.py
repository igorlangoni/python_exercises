import time

def runtimer(function, n=100):
    fun = function
    acc = 0
    c = n
    while c > 0:
        st = time.perf_counter()
        function
        ft = time.perf_counter()
        acc += (ft-st)*1000
        c -= 1
    return (acc/n)*1000


def compare(*args):
    i = 1
    fun = {}
    for arg in args:
        fun[f"func_{i}"] = arg 
        i += 1
    i = 1
    for k, v in sorted(fun.items(), key=lambda x:x[1]):
        print(f"{i}º: {k} --> {v} ms")
        i += 1


