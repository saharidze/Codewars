def find_uniq(arr):
    arr1 = set(arr)
    for i in arr1:
        if arr.count(i) == 1:
            return i
