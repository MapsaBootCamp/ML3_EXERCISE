for i in range(int(input())):
    n,s,a=input().split()
    s=int(s)+((int(n)-1)*int(a))
    s_part=(s/int(n))-int(a)

    if s_part==int(s_part):
        print(int(s_part))
    else:
        print(-1)
