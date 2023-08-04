def sort_array(arr):
    odd_nums = sorted((num for num in arr if num % 2 != 0), reverse=True)
    return [num if num % 2 == 0 else odd_nums.pop() for num in arr]
