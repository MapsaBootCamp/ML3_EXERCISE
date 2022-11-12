

#test_number=int(input())
b=list(map(int,input().split()))
incorrect_a=list(set(b))



def find_a(b,incorrect_a):
    for i in range (0,len(incorrect_a)):
        
        result= find_members(b,incorrect_a,i)
        wrong_path=result[0]
        
        if wrong_path:
            print(result[1])
            break
        else:
            continue

def find_members(b,incorrect_a,i,correct_a=[None for i in incorrect_a]):
    
    correct_a[i]=b[0]
    
    
    b_index_pointer=1
    n=len(incorrect_a)
    real_i=i+1
    while b_index_pointer <len(b):
        print(correct_a)
        
        index_a=(real_i%n+1)
        
        
        if b[b_index_pointer] not in correct_a:
            correct_a[index_a-1]=b[b_index_pointer]
            
            b_index_pointer+=1
            real_i=index_a
        elif b[b_index_pointer] in correct_a and b[b_index_pointer]==correct_a[index_a-1]:
            
            b_index_pointer+=1
            real_i=index_a
        else:
            
            return [False]
    return [True,correct_a]


   

find_a(b,incorrect_a)

