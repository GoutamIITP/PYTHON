import math 
def euclidean_dis(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1]-point1[1])**2)

pointA = (100, 0)
pointB = (85, 15)
distance = euclidean_dis(pointA, pointB)
print(distance)

arr = [130.862, 11.180, 7.071, 106.066, 21.213, 120.208, 102.591, 5.0]
arr.sort()
print(arr)