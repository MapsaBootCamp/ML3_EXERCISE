def smallest_num (k:int) -> int:
  largest_digit = 9
  power = 0
  output = 0
  is_success = False
  while True:
    if k ==0 :
      is_success =True
      break
    if largest_digit == 0:
      break
    if k >= largest_digit:
      output += largest_digit *10**power
      
      k -= largest_digit
      largest_digit -=1
      power += 1
      # print(output,k)
    else:
      largest_digit -=1
  if is_success:
    return output
  return False

print(smallest_num(21))