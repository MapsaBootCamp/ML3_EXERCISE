def Bad_Boy(x:int,y:int,i:int,j:int):
    long_dis=2*(x-1)+2*(y-1)
    print('the long dis:',long_dis) # the distance that anton have to pass  should be equal to long_dist
    arr = [[0 for i in range(y)] for j in range(x)]
    arr[i][j]='A'
    if i<x and j<y:
        i1,j1=x-1,i
        i2,j2=x-1,y-1
        arr[i1][j1]='y1'
        arr[i2][j2] = 'y2'
        for yo1 in arr:
            print(yo1)
    elif i>=x and j>=y:
        i1, j1 = x - 1, j
        i2, j2 =  1, 1
        arr[i1][j1] = 'y1'
        arr[i2][j2] = 'y2'
        for yo1 in arr:
            print(yo1)

#the room demensions
test=int(input('number of test case:'))
for t in range(1,test+1):
    x = int(input('rows:'))
    y = int(input('column:'))
    # Anton's cell
    i = int(input('i:'))-1
    j = int(input('j:'))-1
    Bad_Boy(x,y,i,j)