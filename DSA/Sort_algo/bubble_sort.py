def bubble_sort(arr, n):
    for i in range(n-1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if (did_swap == False):
            break
                
    print("After using bubble_sort Algo")
    print(" ".join(map(str, arr)))
    


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arr)
    print(f"Before using Bubble sort \n {arr}")
    bubble_sort(arr, n)

