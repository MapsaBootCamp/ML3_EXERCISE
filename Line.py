from typing import Tuple
# There are n people in a horizontal line, each looking either to the left or the right. Each person counts the number of people in the direction they are looking. The value of the line is the sum of each person's count.

# For example, in the arrangement LRRLL, where L stands for a person looking left and R stands for a person looking right, the counts for each person are [0,3,2,3,4], and the value is 0+3+2+3+4=12.

# You are given the initial arrangement of people in the line. For each k from 1 to n, determine the maximum value of the line if you can change the direction of at most k people.

# Input
# The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains an integer n (1≤n≤2⋅105) — the length of the line.

# The following line contains a string consisting of n characters, each of which is either L or R, representing a person facing left or right, respectively — the description of the line.

# It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

# Please note that the answer for some test cases won't fit into 32-bit integer type, so you should use at least 64-bit integer type in your programming language (like long long for C++).

# Output
# For each test case, output n space-separated non-negative integers — the maximum value of the line if you can change the direction of at most k people for each k from 1 to n, inclusive.
def element_value(line: str, index: int) -> int:
	if line[index] == 'L':
		return index
	elif line[index] == 'R':
		return len(line) - index - 1

def changed_element_value(line: str, index: int) -> int:
	if line[index] == 'L':
		return len(line) - index - 1
	elif line[index] == 'R':
		return index

def line_value(line: str) -> int:
	value = 0
	for index, char in enumerate(line):
		value += element_value(line, index)
	return value

def max_val_line(test_case: Tuple[int, str], allowed_change: int) -> int:
	length = test_case[0]
	line = test_case[1]
	effect_of_change = []
	for index, char in enumerate(line):
		val = 0
		if element_value(line, index) < changed_element_value(line, index):
			val += changed_element_value(line, index) - element_value(line, index)
		effect_of_change.append((index,val))

	effect_of_change.sort(key = lambda x: x[1])
	line_val = line_value(line)
	for changes in range(1, allowed_change+1):
		line_val += effect_of_change.pop()[1]
	return(line_val)




def maximize_line_value(input_address: str = 'input.txt') -> None:
	with open(input_address, 'r') as input_object:
		content = input_object.readlines()
		_input = [line.rstrip() for line in content]
		count_of_test_cases  = int(_input[0])
		test_cases = [(int(_input[index*2-1]), _input[index*2]) for index in range(1, count_of_test_cases+1)]
	for case in test_cases:
		for i in range(1, case[0]+1):
			print(max_val_line(case, i), end = ' ')
		print()


maximize_line_value(input_address: str = 'input.txt')