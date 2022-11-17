def sum_of_digits(number: int) -> int: 
    digits = str(number)
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum

def unique_digits(number: int) -> bool:
    if number < 10:
        return True
    chars = str(number)
    for index, char in enumerate(chars):
        if index + 1 < len(chars): 
            if char in chars[index+1:]:
                return False
    return True

def next_min_intended_sum(min_number: int, intended_sum: int)-> int:
    flag = True
    while flag:
        min_number += 1
        if sum_of_digits(min_number) == intended_sum:
            flag = False
        
    return min_number

value = input()
number_of_test_cases = int(value)
input_array = []
for i in range(0,number_of_test_cases):
    chars = input()
    input_array.append(chars)
intended_sum = 0
for chars in input_array:
    intended_sum = int(chars)
    ceiling = '9'
    num_of_digits = 1

    while sum_of_digits(int(ceiling)) < intended_sum:
        ceiling += str(int(ceiling[-1])-1)
        num_of_digits += 1

    floor =''
    for i in range(0, num_of_digits):
        floor += str(i+1)

    min_number = int(floor)

    while sum_of_digits(min_number) != intended_sum or ( not unique_digits(min_number) ):

        min_number = next_min_intended_sum(min_number, intended_sum)

    print(min_number)
