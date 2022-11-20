song=input("Enter love song:")
n=int(input("Enter the number of questions:"))
question:list=[]

for i in range(n):
    question.append(tuple(input("Enter questoin:").split()))

Alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

answer:list=[]

for q in range(len(question)):
    for i in range(int(question[q][0]), int(question[q][1])+1):
        answer.append(song[i]*(Alphabet.index(song[i])+1))
    print(''.join(answer))
    answer=[]
