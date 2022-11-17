from typing import Tuple

def anton_distance(anton: Tuple[int, int], yoyo1: Tuple[int, int], yoyo2: Tuple[int, int])-> int:
	step_one = abs(anton[0] - yoyo1[0]) + abs(anton[1]-yoyo1[1])
	step_two = abs(yoyo2[0] - yoyo1[0]) + abs(yoyo2[1]-yoyo1[1])
	step_three = abs(anton[0] - yoyo2[0]) + abs(anton[1]-yoyo2[1])
	return (step_one + step_two + step_three)


def bad_boy(case: Tuple[int, int, int, int])-> str:
    (rows, columns, x,y) = case
    max_distance = 0
    yoyo1 = (0,0)
    yoyo2 = (0,0)
    candidates = [(columns, rows), (columns, 1), (1, rows), (1, 1)]

    for candidate1 in candidates:
    	for candidate2 in candidates:
    		if max_distance < anton_distance((x, y), candidate1, candidate2):
    			max_distance = anton_distance((x, y), candidate1, candidate2)
    			yoyo1, yoyo2 = candidate1, candidate2
    

    # for x1 in range(1, columns + 1):
    # 	for y1 in range(1, rows + 1):
    # 		for x2 in range(1, columns + 1):
    # 			for y2 in range(1, rows + 1):
    # 				if max_distance < anton_distance((x, y), (x1, y1), (x2, y2)):
    # 					max_distance = anton_distance((x, y), (x1, y1), (x1, y2))
    # 					yoyo1, yoyo2 = (x1, y1), (x2, y2)

    return f'{yoyo1[0]} {yoyo1[1]} {yoyo2[0]} {yoyo2[1]}'


num_of_lines = int(input())
lines = []
for case_index in range(0, num_of_lines):
	lines.append(input())
cases = []
for line in lines:
	n, m, i, j = int(line.split()[0]), int(line.split()[1]), int(line.split()[2]), int(line.split()[3])
	cases.append((n, m, i, j))

for case in cases:
    print(bad_boy(case))
# given cases