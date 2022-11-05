def info(n:int, line:str)->str:
    info = (line[:n] + '')
    return info
while True:
    try:
        n = int(input('enter lenght of string:'))
        line = input('enter line(L/R):')
        print(info(n, line))
        break
    except Exception:
        print('enter input in correct format')
        continue

def Left(num:int)->str:
    return info[:num]

def Right(numm:int)->str:
    return info[numm + 1:]

def init_val(info:str)->int:
    init_l = []
    for i in range(len(info)):
        if info[i] == 'L':
            str = Left(i)
            init_l.append(len(str))
        elif info[i] == 'R':
            str1 = Right(i)
            init_l.append(len(str1))
    initial_val = sum(init_l)
    print(f'the  value is {init_l} and sum of them is: {initial_val}')
    return initial_val


info = info(n, line)
init = init_val(info)

def change_direction():
    info1 = ''
    info2=''
    for i in range(len(info)):
        if i == 0:
            if info[i] == "L":
                info1 = 'R' + info[1:]
                print(info1)
            elif info[i] == 'R':
                info1 = 'L' + info[1:]
                print(info1)
        if i==1:
            if info1[-i] == "L":
                info2 = info1[:-1]+'R'
                print(info2)
            elif info[-i] == 'R':
                info2 = info1[:-1] + 'L'
                print(info2)

    first_val = init_val(info1)
    sec_val = init_val(info2)
    for i in range(len(info)):
        if first_val > init and sec_val>first_val:
            print(sec_val, end=' ')
        elif first_val > init and sec_val<first_val:
            print(first_val,end=' ')
    return sec_val

first_val = change_direction()






