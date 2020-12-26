import math


def find_distance(circle, point1, point2):
    # if point1[0] == point2[0] and point1[0] == circle[0]:
    #  return False
    # elif point1[1] == point2[1] and point1[1] == circle[1]:
    #    return False
    # else:
    distance_y = point1[1] - point2[1]
    distance_x = point1[0] - point2[0]
    chisl = math.fabs(distance_y * circle[0] - distance_x * circle[1] + point2[0] * point1[1] - point2[1] * point1[0])
    znam = math.sqrt(distance_y ** 2 + distance_x ** 2)

    return chisl / znam


def func(rad, circle, points):
    l = [[math.fabs(circle[0] - t[0]), math.fabs(circle[1] - t[1])] for t in points]

    inside = 0

    for distance in l:
        if math.sqrt(distance[0] ** 2 + distance[1] ** 2) == rad:
            return "YES"
        elif math.sqrt(distance[0] ** 2 + distance[1] ** 2) < rad:
            inside += 1

        # else:
        #   outside += 1
        #  outside_m[l.index(distance)] = distance
    if inside in range(1, 3):
        return "YES"
    if inside == 0:
        i = 0
        add = 1
        while i != 2:
            while i + add != 3:

                d = find_distance(circle, points[i], points[i + add])

                if d <= rad:  # and d != 0:

                    return "YES"
                add += 1
            i += 1
            add -= 2

    return "NO"


for i in range(int(input())):
    circle_ar = [float(el) for el in input().split()]
    points = []
    for i in range(3):
        points.append([float(el) for el in input().split()])
    print(func(circle_ar[2], circle_ar[:2], points))
