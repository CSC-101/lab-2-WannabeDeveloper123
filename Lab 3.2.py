def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total
#num = 4, 9, 2, 1
#total = 4, 13, 15, 16

result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above? adding a list as an element instead of adding integers as an element instead.
#we're also creating a new list to store changes instead of modifying the old one.
#new_list = [4], [4,9], [4,9,2], [4,9,2,1]
#idx = 4, 9, 2, 1
result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
    return new_list
#new_list = [5, 10, 3, 2]
#value = [4,9,2,1]
result = increment_all([4, 9, 2, 1])

