t= int(input())
lst=[]
lst1=[]
for i in range(t):
    s=[]
    z=int(input())
    a=input().split(" ")
    for i in a:
        s.append(int(i))
    lst.append(s)
for i in lst:
    flag=False
    lst2=[]
    for j in range(len(i)):
        if len(lst2)>= 1:
                break
        for k in range(len(i)):
            if len(lst2)>= 1:
                break
            if j!=k and i.index(i[j])==i.index(i[k]):
                lst1.append((i[j:k]))
                lst2.append((i[j:k]))
                flag=True
                break
    if flag == False:
        lst1.append(i)
                
for i in lst1:
    print(len(i))
    for j in i:
        print(j,end=" ")
        
    print()
    
            
   
