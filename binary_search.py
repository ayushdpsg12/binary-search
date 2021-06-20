def BinarySearch(arr, lower, higher, key):
    if higher >= lower:
        mid = (lower+higher)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return BinarySearch(arr, lower, mid-1, key)
        else:
            return BinarySearch(arr, mid+1, higher, key)
    else:
        return -1


n = int(input("Enter no of integers in array:"))
arr = []

for i in range(n):
    a = int(input("Enter the integer:"))
    arr.append(a)

arr.sort()

print(arr)

key = int(input("Enter the integer you want to search:"))

lower = 0
higher = n

k = BinarySearch(arr, lower, higher, key)

print(k)
