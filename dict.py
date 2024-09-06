# def BubbleSort(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lst[j] < lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]


# lst = [3, 67, 80, 5, 8, 1, 35]
# BubbleSort(lst)
# print("Sorted array", lst)


def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >=0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key


lst = [3, 67, 80, 5, 8, 1, 35]
insertionSort(lst)
print("Sorted array", lst)