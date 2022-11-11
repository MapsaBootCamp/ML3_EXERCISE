t = int(input())
for i in range(t):
    n, S, a = map(int, input().split(" "))
    if (int((S - a) / n) != (S - a) / n) or S - a <= 0:
        print(-1)
    else:
        print(int((S - a) / n))
