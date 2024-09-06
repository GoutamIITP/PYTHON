# arr = [2,4,1,3,5]
# arr = [1, 3, 4 ,5 ,6]

# def is_sorted(arr):
#     return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# if (is_sorted(arr)):
#     print("yes")
# else:
#     print("No")

# n = len(arr)
# d = n % 2
# def leftrotate(arr, d, n):
#     for i in range(d):
#         rotateone(arr, n)

# def rotateone(arr, n):
#     temp = arr[0]
#     for j in range(n - 1):
#         arr[j] = arr[j + 1]
#     arr[n - 1] = temp


# leftrotate(arr, d, n)
# print(arr)

arr = [1, 3, 4, 5, 6]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted(arr))
