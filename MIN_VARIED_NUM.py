import itertools
def min_varied_num(number:int):
    list_of_den = []
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 1
    sum_of_num = []
    sum_of_density = []

    for j in num:
        den=j/number
        list_of_den.append(den)
    for l in range(1,len(num)):
        for seq in itertools.combinations(num, l):
            if sum(seq)==number:
                sum_of_num.append(seq)

    for h in range(1, len(list_of_den)):
        for seqq in itertools.combinations(list_of_den, h):
            if sum(seqq) == target:
                sum_of_density.append(seqq)
    sum1=sum_of_num[0]
    for i in sum1:
        print(i,end='',)
def main():
    while True:
        try:
            n=int(input('enter number of questions:'))
            for i in range(1,n+1):
                number=int(input('enter number(between 1 to 44):'))
                min_varied_num(number)
                print()
            break
        except Exception:
            print('enter in correct format')
            continue
main()














