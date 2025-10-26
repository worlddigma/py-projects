def bynarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int(( low + high ) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item: 
            low = mid + 1
        else:
            high = mid - 1
    return None

mylist = [0, 0, 3, 0, 0]
print(bynarySearch(mylist, 3))