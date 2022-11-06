# https://codeforces.com/problemset/problem/1537/B
def Bad_boy():
    n, m, i, j = input(
        "Enter rooms dimentions and Enter Antons position: : ").split(" ")
    i = int(i)
    j = int(j)
    m = int(m)
    n = int(n)
    corners = [[0, 0], [0, m], [n, 0], [n, m]]
    temp1 = [[0, 0], 0]
    temp2 = [[0, 0], 0]
    for k in range(0, 4):
        if temp1[1] < abs(i - corners[k][0] + j - corners[k][1]):
            temp1[1] = abs(i - corners[k][0] + j - corners[k][1])
            temp1[0][0] = corners[k][0]
            temp1[0][1] = corners[k][1]
    corners.remove(temp1[0])
    i = temp1[0][0]
    j = temp1[0][1]
    for k in range(0, 3):
        if temp2[1] < abs(i - corners[k][0] + j - corners[k][1]):
            temp2[1] = abs(i - corners[k][0] + j - corners[k][1])
            temp2[0][0] = corners[k][0]
            temp2[0][1] = corners[k][1]

    print(temp1)
    print(temp2)


Bad_boy()
