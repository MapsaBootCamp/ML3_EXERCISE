a=input().split()
for i in range(1,len(a)):
    if a[0]==a[i]:
        result=a[0:i]
        print(len(result))
        print(a[0:i])
        break
    
