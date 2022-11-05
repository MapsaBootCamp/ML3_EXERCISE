def calc_score(s:str) ->str:
  l = len(s)
  score = 0
  for i in range(len(s)):
    if s[i] == "r":
      score += l-i -1
    elif s[i] == "l":
      score += i
  return score


def costume_index(s:str) -> list:
  # print(len(s))
  ind_1 = list(range(len(s)//2))
  ind_2 = list(range(len(s)-1,(len(s)//2)-1,-1))
  inds = list(zip(ind_1, ind_2))
  return [sub_item  for item in inds for sub_item in item]


def optimizer(input_string : str , k : int):
  index = costume_index(input_string)
  input_string_lst = list(input_string)
  length = len(input_string)
  moves = 0 
  optimal_char = ""
  for i in index:
    if k == 0 :
      break
    optimal_char = "r" if i < length/2 else "l"
    if input_string_lst[i] != optimal_char:
      input_string_lst[i] = optimal_char
      k -= 1
      moves +=1

  

  out= "".join(input_string_lst)
  return  moves , out , calc_score(out)


for k in range(11):
    print(optimizer("rlrrllr",k))
