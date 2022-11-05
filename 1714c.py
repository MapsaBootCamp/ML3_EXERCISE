# number= int(input("plz enter ur number:"))
number=45
def findnumber(number):
    result=[]
    if (number)<10:
        return(number)
    else:
        for i in range(9,0,-1):
            result.append(i)
            # print(i,result)
            if sum(result)== number:
                return (result[::-1])
            elif number-sum(result) <9:
                if (number-sum(result)) not in result:
                    result.append(number-sum(result))
                    # print(i,result)
                    return (result[::-1])


print(findnumber(number))