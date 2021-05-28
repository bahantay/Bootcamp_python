def find_pivot(param_1, param_2):
    total_sum = sum(param_1)
    left_sum = 0
    for i, num in enumerate(param_1):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num
    return -1


list = [1, 2, 3, 4, 0, 6]
num = 6
print(find_pivot(list, num))
