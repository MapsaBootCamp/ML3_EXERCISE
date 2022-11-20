sum=int(input("Enter the sum:"))

def Minimum_digit(s:int) -> list:
    n:list=[]
    i=9
    for i in range(9,0,-1):
        if s-i>0:
            n.append(str(i))
            s-=i
        elif s-i<0:
            pass
        elif s-i==0:
            n.append(str(i))
            break
    n.reverse()
    return n

print("".join(Minimum_digit(sum)))