def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? none of the calls
    else:
        return m

first = smallest(3, 2)       # What is the value of first? first = 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? second = 2
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement? when function is called in var answer1
    elif b > c:
        return b + c             # In general, when will a call to this function evaluate this statement? when function is called in var answer2
    else:
        return 2 * c             # In general, when will a call to this function evaluate this statement? when function is called in var answer3


answer1 = function2(3, 2, 1)     # What is the value of answer1? answer1 = 1
answer2 = function2(2, 3, 1)     # What is the value of answer2? answer2 = 4
answer3 = function2(2, 1, 3)     # What is the value of answer3? answer3 = 6
print()