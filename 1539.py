n,q=input().split(" ")
song=input()
first_str=""
second_list=[]
if len(song)==int(n):
    
    for i in range(int(q)):
        first,last=input().split(" ")
        for j in song[int(first)-1:int(last)]:
            first_str+=((ord(j)-96)*j)
        second_list.append(first_str)
        first_str=""
    for i in second_list:
        print(len(i))
    