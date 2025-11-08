def Sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + Sum(arr[1:])
    
arr = [1, 2, 3, 4]
print(Sum(arr))