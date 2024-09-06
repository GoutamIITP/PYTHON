def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        temp = arr[min]
        arr[min] =  arr[i]
        arr[i] = temp

    print("After selection sort")
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    print("Before selection sort")
    print(" ".join(map(str, arr)))

    selection_sort(arr)