for _ in range(int(input())):
    number=int(input())
    result=""
    temp=9
    while number>temp:
        result=str(temp)+result
        number=number-temp
        temp=temp-1
    print(str(number)+result)
        
