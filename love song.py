

length_and_questions=list(map(int,input('please give me the length of the song and the number of questions\n').split()))
song=input('please give the song\n')

total_bounds=[]
for i in range (0,length_and_questions[1]):
    bounds=list(map(int,input('please give me the bounds of the question.\n').split()))
    total_bounds+=[bounds]
def lenght (song,start_index,end_index):
    total_lenght=0
    for i in range (start_index-1,end_index):
        total_lenght+=ord(song[i])-96
    return total_lenght

for i in range(0,length_and_questions[1]):
    print(lenght(song,total_bounds[i][0],total_bounds[i][1]))

