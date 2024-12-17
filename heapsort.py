def toHeap(arr, n, i):
    root = i  
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        root = l
    if r < n and arr[root] < arr[r]:
        root = r
    if root != i:
        (arr[i], arr[root]) = (arr[root], arr[i])  # swap
        toHeap(arr, n, root)
 
def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2, -1, -1):
        toHeap(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        toHeap(arr, i, 0)

def extractNums(nums:str):
    nums2=nums.replace("  ", " ")
    nums3=nums2.split(" ")
    nums4=[int(i) for i in nums3]
    return nums4
print("Enter the numbers to sort sperated by spaces")
usrinp=input()
arr=extractNums(usrinp)
heapSort(arr)
print(arr)
