line_Of_People=list(input("Enter the line of people:"))

def Max_Value(people: list):
    n=len(people)
    v=''
    people_temp=people.copy()
    for k in range(n):
        j=k
        zl=0
        zr=n-1
        r='begin'
        while (k!=-1):
            if zl==n//2 and zr==n//2:
                break
            if people[zl]=='L' and r=='begin':
                people[zl]='R'
                k-=1
                r='end'
                zl+=1
            elif people[zl]=='R' and r=='begin':
                zl+=1
                r='end'
            elif people[zr]=='R' and r=='end':
                people[zr]='L'
                k-=1
                r='begin'
                zr-=1
            elif people[zr]=='L' and r=='end':
                zr-=1
                r='begin'
        k=j
        print("".join(people))

        value=0
        for i in range(n//2+1):
            if people[i]=='R':
                value+=n-i-1
            else:
                value+=i
        for i in range(n-1,n//2,-1):
            if people[i]=='L':
                value+=i
            else:
                value+=n-i-1
        v=v+str(value)+" "     

        people=people_temp.copy()

    print(v)

Max_Value(line_Of_People)
                

