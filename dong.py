def app (x,y,z):
    h=int(y)//(int(x)-1)
    d=0
    for i in range(h//2-(h//4),(h+h//2)):
        for j in range(h//2-(h//4),(h+h//2)):
            if i+((int(x)-1)*j) == int(y) and i==j+int(z):
                d=j
    if d == 0:
        return -1
    else:
        return d
t=int(input())
list1=[]
for i in range(t):
    n,s,a=input().split(" ")
    list1.append(app(n,s,a))
for i in list1:
    print(i)
    