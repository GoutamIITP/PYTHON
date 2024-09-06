# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j , end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(i , end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 6-i+1):
#         print(j, end=" ")
#     print()

# start = 1
# for i in range(1,6):
#     if (i % 2 !=0):
#         start = 1
#     else:
#         start = 0
#     for j in range(i):
#         print(start, end=" ")
#         start = 1 - start
#     print()


# N = 5
# sum = 0
# for i in range(1,N+1):
#     sum +=i
# print(sum)

N = 6
for i in range(6):
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end=" ")
    print()

print(ord('B'))