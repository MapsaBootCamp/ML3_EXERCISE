n=int(input("Enter row of room:"))
m=int(input("Enter column of room:"))
i=int(input("Enter row position of Anton:"))
j=int(input("Enter column position of Anton:"))

# First yoyo
p1=abs(n-i)+abs(m-j)
p2=abs(1-i)+abs(1-j)
p3=abs(n-i)+abs(1-j)
p4=abs(1-i)+abs(m-j)
mainPosition=max(p1,p2,p3,p4)
if mainPosition==p1:
    x1=n
    y1=m
elif mainPosition==p2:
    x1=1
    y1=1
elif mainPosition==p3:
    x1=n
    y1=1
elif mainPosition==p4:
    x1=1
    y1=m

# Second yoyo
p1=abs(n-x1)+abs(m-y1)
p2=abs(1-x1)+abs(1-y1)
p3=abs(n-x1)+abs(1-y1)
p4=abs(1-x1)+abs(m-y1)
mainPosition=max(p1,p2,p3,p4)
if mainPosition==p1:
    if not ((i==n) and (j==m)):
        x2=n
        y2=m
    elif ((i==n) and (j==m)):
        if m>1:
            x2=n
            y2=m-1
        elif n>1:
            x2=n-1
            y2=m
        else:
            x2=1
            y2=1
elif mainPosition==p2:
    if not ((i==1) and (j==1)):
        x2=1
        y2=1
    elif (i==1 and j==1):
        if m>1:
            x2=1
            y2=2
        elif n>1:
            x2=2
            y2=1
        else:
            x2=1
            y2=1
elif mainPosition==p3:
    if not ((i==n) and (j==1)):
        x2=n
        y2=1
    elif (i==n and j==1):
        if m>1:
            x2=n
            y2=2
        elif n>1:
            x2=n-1
            y2=1
        else:
            x2=1
            y2=1
elif mainPosition==p4:
    if not ((i==1) and (j==m)):
        x2=1
        y2=m
    elif (i==1 and j==m):
        if m>1:
            x2=1
            y2=m-1
        elif n>1:
            x2=2
            y2=1
        else:
            x2=1
            y2=1

print("x1: "+str(x1))
print("y1: "+str(y1))
print("x2: "+str(x2))
print("y2: "+str(y2))