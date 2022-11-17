song_length, question_count = (int(i) for i in input().split())
song = input()
segments = []
for k in range(0, question_count):
    segments.append(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'


for i in segments:
    answer_len = 0
    segment = i.split()
    for letter in song[int(segment[0])-1:int(segment[1])]:
        answer_len += alphabet.find(letter) + 1
    print(answer_len)
