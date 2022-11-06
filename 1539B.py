n, q = map(int, input().split(" "))
s = " ".join(input()).split(" ")
for i in range(q):
    l, r = map(int, input().split(" "))
    index_l = l - 1
    index_r = r - 1
    answer = 0
    for j in s[index_l: index_r + 1]:
        answer += ord(j) - 96
    print(answer)
