list_=[1,2,3,4,5,6,7,8,9]
list_.reverse()
input_number=int(input())
input_list=[]
def numdigit(n:int)->list:
    templist=[]
    for i in list_:
        if i <= n:
            templist.append(i)
            n-=i
    return templist
for i in range (input_number):
    input_list.append(int(input()))
newtemplist = []    
for i in input_list:
    newtemplist=numdigit(i)
    newtemplist.reverse()
    for j in newtemplist :
        print(j,end="")
    print()    

    
    