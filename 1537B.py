def distant(point: tuple, position: tuple):
    return abs(point[0] - position[0]) + abs(point[1] - position[1])


n = int(input())
for u in range(n):
    n, m, i, j = map(int, input().split(" "))
    anton = (i, j)
    points = [(1, 1), (1, m), (n, m), (n, 1)]
    first_yoyo = None
    mx = 0
    for t in points:
        if distant(t, anton) >= mx:
            # print("1sssss :", t, mx)
            mx = distant(t, anton)
            first_yoyo = t
    points.remove(first_yoyo)
    second_yoyo = None
    mx = 0
    for t in points:
        if (distant(t, anton) + distant(t, first_yoyo)) >= mx:
            mx = distant(t, anton) + distant(t, first_yoyo)
            second_yoyo = t
            # print("2ssssss :0", t, mx)
    for i in first_yoyo:
        print(i, end=" ")
    for i in second_yoyo:
        print(i, end=" ")
    print("")
