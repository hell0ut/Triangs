from math import fabs,sqrt


def find_distance(circle, point1, point2):
    # if point1[0] == point2[0] and point1[0] == circle[0]:
    #  return False
    # elif point1[1] == point2[1] and point1[1] == circle[1]:
    #    return False
    # else:
    distance_y = point2[1] - point1[1]
    distance_x = point2[0] - point1[0]
    chisl = fabs(distance_y * circle[0] - distance_x * circle[1] + point2[0] * point1[1] - point2[1] * point1[0])
    znam = sqrt(distance_y ** 2 + distance_x ** 2)

    return chisl / znam


def perpendicularToLineAllowed(circle,pt1,pt2):
    line1=(circle[0]-pt1[0])**2+(circle[1]-pt1[1])**2
    line2=(circle[0]-pt2[0])**2+(circle[1]-pt2[1])**2

    if line1<line2:
        vec1_x=circle[0]-pt1[0]
        vec1_y=circle[1]-pt1[1]
        vec2_x = pt2[0] - pt1[0]
        vec2_y = pt2[1] - pt1[1]
    else:
        vec1_x=circle[0]-pt2[0]
        vec1_y=circle[1]-pt2[1]
        vec2_x = pt1[0] - pt2[0]
        vec2_y = pt1[1] - pt2[1]
    angle=(vec1_x*vec2_x+vec1_y*vec2_y)/(sqrt(vec1_x**2+vec1_y**2)*sqrt(vec2_x**2+vec2_y**2))
    return angle>=0


def func(rad, circle, points):
    l = [[fabs(circle[0] - t[0]), fabs(circle[1] - t[1])] for t in points]

    inside = 0

    for distance in l:
        dist= sqrt(distance[0] ** 2 + distance[1] ** 2)
        if  fabs(dist - rad) < 0.01:
            return "YES"
        if dist < rad:
            inside += 1

        # else:
        #   outside += 1
        #  outside_m[l.index(distance)] = distance
    if inside == 3:
        return 'NO'
    elif inside in range(1, 3):
        return "YES"
    elif inside == 0:
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if perpendicularToLineAllowed(circle, points[i], points[j]):
                    d = find_distance(circle, points[i], points[j])
                    if d <= rad:
                        return "YES"
    return 'NO'





for i in range(int(input())):
    circle_ar = [int(el) for el in input().split()]
    points = []
    for j in range(3):
        points.append([int(el) for el in input().split()])
    print(func(circle_ar[2], circle_ar[:2], points))
