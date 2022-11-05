from typing import List
def arrsort(a):
    
    b=[]
    c=[]
    for i in range(1,(len(a)//2)+1):
        
        b.append(a[-i])
    if len(a)%2==0:
        
        s=a[:(len(a)//2)]
    else:
        s=a[:(len(a)//2)+1]
    
    for i in range(len(s)):
        try:
            c.append(s[i])
            c.append(b[i])
        except:
            c.append(s[i])
    if len(b) != len(s):
        c.pop(-1)
    return c

def check_optimal(lst):
    c=1
    d=1
    if len(lst)%2==0:
        for i in range(len(lst)//2):
            if lst[i]!="R":
                c=0
            
            if lst[i+(len(lst)//2)]!="L":
                d=0
            
        if c and d == 1:
            return True
        return False
    else:
        for i in range(len(lst)//2):
            if lst[i]!="R":
                c=0
            
            if lst[i+1+(len(lst)//2)]!="L":
                d=0
            
            
        if (c and d) == 1:
            return True
        return False

def ready_for_counting(list1,K):
    count=0
    for i in range(1,K+1):
        while count != i:
            j=0
            while j == len(list1) or count != i:
                if (j %2 )== 0:
                    if list1[j] == "L":
                        list1[j]="R"
                        count+=1


                else:
                    if list1[j] == "R":
                        list1[j] = "L"
                        count+=1

                j+=1
    return list1



def backtonormal(liste):
    a=[]
    b=[]
    c=[]
    for i in range(len(liste)):
        if i%2 == 0:
            a.append(liste[i])
        else:
            b.append(liste[i])
    b.reverse()
    
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
        
    
    return c
def countvalue(lst):
    a=[]
    b=0
    for i in range(len(lst)):
        if lst[i]=="R":
            a.append(len(lst[i+1:]))
        else:
            a.append(len(lst[:i]))
    for i in a:
        b+=i
    return b


inputnum=int(input())
result=[]
for counter in range(inputnum):
    
    templist=[]
    lenghtcounter=int(input())
    inputstr=input()
    for elm in inputstr:
        templist.append(elm)
    arr=templist.copy()
    sortedlist=arrsort(arr)
    
    
    normaled=["L","L","L"]
    stri=""
    for k in range(1,len(templist)+1):
        if len(inputstr) == 1:
            stri="0 "
            break
        
        g=sortedlist.copy()
        
        
        if not check_optimal(normaled):
            
            readylist=ready_for_counting(g,k)
            
            normaled=backtonormal(readylist)
            
            s=countvalue(normaled)
            stri+=(str(countvalue(normaled))+" ")
        else:
            
                
            stri+=(str(s)+" ")
    result.append(stri)
            
for i in result:
    a=(i.split(" ")[:-1])
    for j in a:
        print(j,end=" ")
    print()

       
        
