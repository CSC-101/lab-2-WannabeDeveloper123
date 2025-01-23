more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. 1+1, 2+1, 3+1, 4+1
print()                               # What is the value of more at this point? [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and 1-1, 2-4, 3-9, 4-16
                                           # the corresponding return value.

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the [1,4,9,16]
print()                                    # values recorded above?

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and 0-False, 1-False, 2-False, 3-True, 4-True
                                             # the corresponding return value. returns 3 and 4

answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3, 4]
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and 3+1 = 4, 4+1 = 5
                                             # the corresponding return value.
def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and 0-False, 1-False, 2-False, 3-True, 4-True
                                             # the corresponding return value.

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print()