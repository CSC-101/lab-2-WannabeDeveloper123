from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? False on first, True on second
    if test:                            # What is this check preventing? preventing from entering if loop to prevent index out of range error
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? None
second = checked_access([1, 0, 1], 2)    # What is the value of second? 1
print(first, second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated ans: first
    elif len(L) > 1:                                  #   and what are the values being added? "this", "is", "the"
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated ans: second
    elif len(L) > 0:                                  #   and what are the values being added? "second call"
        result = len(L[0])                            # For which call below is this statement evaluated ans: third
    else:                                             # and what are the values being added? "another", "call"
        result = 0
    return result


#first = length_sum(["this", "is", "the", "first", "call"])
#second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
#first = surprising(words, "Avoid")
#second = surprising(words, "such.")
         # What is the value of words at this point? ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
         # What are the values of first and second at this point? first and second share same value as the list words.
         # What happened? list is mutable, reflecting changes due to the function call in second to the call in first.
print()