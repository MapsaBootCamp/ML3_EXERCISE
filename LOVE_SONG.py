def info(num_len:int,lett:str)->str:
    info = (lett[:num_len] + '')
    return info
while True:
    try:
        num_of_len=int(input('enter lenght of string:'))
        num_of_question=int(input('number of question:'))
        letter=input('enter string:')
        info = info(num_of_len, letter)
        print(info)
        break
    except Exception:
        print('enter input in correct format')
        continue
def love_song(info:str):
    final_str=[]
    last_str=[]
    result=''
    ch='abcdefghijklmnopqrstuvwxyz'
    #for loop according to number of questions
    for num_q in range(1,num_of_question+1):
        start=int(input('first index:'))
        last=int(input('last index:'))
        new_info=(info[start-1:last])
        final_str.clear()
        final_str.append(new_info)
        for chh in final_str:
            for char in chh:
                new_index=ch.index(char)+1
                last_str.append(char*new_index)
        print(result.join(last_str),len(result.join(last_str)))
        last_str.clear()

love_song(info)




