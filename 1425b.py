def onerun(df, rst, bst, counter, turn,strhis,tryno):  # rst: Red Status bst:Blue Status
    finish = 1

    for col in range(tryno,len(df)):
        if df[rst][col].startswith('1') and turn == 'R':
            counter += 1
            df[rst][col], df[col][rst] = 'R' + str(counter), 'R' + str(counter)
            strhis = strhis + 'R' + str(rst) + str(col)
            rst = col
            turn = 'B'
            finish = 0

            break
    for col in range(len(df)):
        if df[bst][col].startswith('1') and turn == 'B':
            counter += 1
            df[bst][col], df[col][bst] = 'B' + str(counter), 'B' + str(counter)
            strhis = strhis + 'B' + str(bst) + str(col)
            bst = col
            turn = 'R'
            print('bst', bst)
            finish = 0

            break

    return (df, rst, bst, counter, turn, finish,strhis)


import pandas as pd

node = 5
relno = 6
rel = [1, 2, 2, 3, 3, 4, 4, 1, 1, 5, 5, 1]
l = (int(len(rel) / 2))
counter, result = 0, 0
rel = [x - 1 for x in rel]
df = pd.DataFrame([['' for i in range(1, node + 1)] for i in range(1, node + 1)])
# print(rel)
for i in range(l):
    df[rel[2 * i]][rel[2 * i + 1]] += '1'
    df[rel[2 * i + 1]][rel[2 * i]] += '1'
print(df)
turn = 'R'

dfmain = df.copy()

arrhistoey=[]
tryno=0
for all in range(2*int(len(df))):

    df=dfmain.copy()
    counter,rst, bst = 0, 0,0
    strhis = ''
    for row in range(int(len(df))):
        df, rst, bst, counter, turn, finish,strhis = onerun(df, rst, bst, counter, turn,strhis,tryno)


        if finish == 1:
            result += 1
            arrhistoey.append(strhis)

            break
        print('----------------------rst,bst,counter', rst, bst, counter,strhis)
        print(df)


    # print('----------------------rst,bst,counter', rst, bst, counter)
    print(arrhistoey,'tryno',tryno)
    tryno+=1
# print('sum:',counter)