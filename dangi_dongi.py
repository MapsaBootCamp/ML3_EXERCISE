

details=list(map(int,input('please give the details\n').split()))



def check (details):

    people=details[0]
    cost=details[1]
    Transactin_fee=details[2]
    proportion=(cost/people)-(Transactin_fee/people)
    
    if proportion-int(proportion)!=0 or proportion<=0  :
        return -1
    else:
        return proportion


print(check(details))