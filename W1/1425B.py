m=int(input("number of routes:"))
n=int(input("number of checkpoints:"))

routes:list=[]
Blues:list=[]
Reds:list=[]
firstCheckPoints:list=[]
nextCheckPointsForBlue:list=[]
nextCheckPointsForRed:list=[]

for i in range(m):
    routes.append(tuple(int(item) for item in input("Enter checkpoints:").split()))

def Find_Config(routes:list, startpoint:int, which:str):
    for i in range(len(routes)):
        if routes[i][0]==startpoint:
            firstCheckPoints.append(routes[i])
    if firstCheckPoints[0] and firstCheckPoints[1] and which=='both':
        Blues.append(firstCheckPoints[0])
        routes.remove(firstCheckPoints[0])
        Reds.append(firstCheckPoints[1])
        routes.remove(firstCheckPoints[1])
        Find_Config(routes, firstCheckPoints[0][1], 'blue')
        Find_Config(routes, firstCheckPoints[1][1], 'red')
    elif firstCheckPoints[0] and not firstCheckPoints[1] and which=='blue':
        Blues.append(firstCheckPoints[0])
        routes.remove(firstCheckPoints[0])
        Find_Config(routes, firstCheckPoints[0][1], 'blue')
    elif firstCheckPoints[0] and not firstCheckPoints[1] and which=='red':
        Reds.append(firstCheckPoints[0])
        routes.remove(firstCheckPoints[0])
        Find_Config(routes, firstCheckPoints[0][1], 'red')
    elif not firstCheckPoints[0]:
        return (Blues,Reds)

Find_Config(routes, 1, 'both')

print("Blue:")
print(Blues)
print("\nRed:")
print(Reds)



