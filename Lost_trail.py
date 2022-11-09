import collections
n=int(input('enter number of test:'))
for i in range(1,n+1):
    while True:
        try:
            num = int(input('enter lenght of list:'))
            a = [int(x) for x in input('num:').split()]
            if len(a)>num or len(a)<num:
                print('the lenght is not correct')
                continue
            else:
                l=set(a)
                lenght=len(l)
                empty=[]
                a_list = collections.deque(a)
                a_list.rotate(lenght-1)
                for j in a_list:
                    if j not in empty:
                        empty.append(j)
                if len(a)==len(empty):
                    for j in a:
                        print(j,end=' ')
                    print()
                    print('the lenght is:',len(a))
                    break
                print('the lenght is:',lenght)
                for i in empty:
                    print(i,end=' ')
                print()
            break
        except Exception:
            print('enter correct format')
            continue




