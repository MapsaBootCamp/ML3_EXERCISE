howMany=int(input())
e=[]
for i in range(howMany):
    a,b,c,d=input().split(" ")
    e.append((int(a),int(b),1,1))
for i in e:
    for j in i:
        print(f"{j} ",end="")
    print()