''' Using Figure 7.1 as a model, illustrate the operation of PARTITION on the array
A = (13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11).'''
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
quicksort(A,0,len(A)-1)
print(A)