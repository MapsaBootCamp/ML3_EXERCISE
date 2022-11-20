a,b=input().split()
note=input()
for i in range(int(b)):
    start,end=input().split()
    result=0
    for j in range(int(start)-1,int(end)):
        result=ord(note[j])-96+result
    print(result)
