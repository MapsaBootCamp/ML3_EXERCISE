def dang_o_dong(n:int,s:int,a:int):
    pay=(((n-1)*a)+s)/n
    output=pay-a
    madar_kharj=s-((n-1)*output)
    if madar_kharj==pay:
        return output
    elif madar_kharj>pay:
        return -1
    elif s<=a:
        return -1
def main():
    t=int(input('enter number of test:'))
    for i in range(1,t+1):
        while True:
            try:
                people=int(input('enter num of people:'))
                cost=int(input('enter cost:'))
                wage=int(input('enter wage:'))
                print(dang_o_dong(people,cost,wage))
                break
            except Exception:
                print('enter in correct format')
                continue
main()
