# https://codeforces.com/problemset/problem/1722/D
def Result_count(People: str) -> int:
    result: int = 0
    for i in range(0, len(People)):
        if People[i] == "L":
            result += i
        elif People[i] == "R":
            result += len(People) - i - 1
    return result


def D_line() -> list:
    People = input("Please enter the description of the line:")
    result_list = []
    for i in range(0, len(People)):
        if i < len(People)/2:
            #text = text[:1] + 'Z' + text[2:]
            People = People[:i] + 'R' + People[i+1:]
            #People = "R"
        else:
            People = People[:i] + 'L' + People[i+1:]
            #People[i] = "L"
        result_list.append(Result_count(People))
    print(result_list)
    return result_list


def D_line_greedy() -> list:
    People = input("Please enter the description of the line:")
    result_list = []
    result = Result_count(People)
    for i in range(0, len(People)):
        if People[i] == "L":
            People = People[:i] + 'R' + People[i+1:]
            if Result_count(People) > result:
                result = Result_count(People)
            else:
                People = People[:i] + 'L' + People[i+1:]
        if People[i] == "R":
            People = People[:i] + 'L' + People[i+1:]
            if Result_count(People) > result:
                result = Result_count(People)
            else:
                People = People[:i] + 'R' + People[i+1:]
        result_list.append(Result_count(People))
    print(result_list)
    return result_list


def D_line_better() -> list:
    People = input("Please enter the description of the line:")
    result_list = []
    result = Result_count(People)
    for i in range(0, int(len(People)/2)):
        if People[i] == "L":
            People = People[:i] + 'R' + People[i+1:]
            print(People)
            # if Result_count(People) > result:
            result = Result_count(People)
        result_list.append(result)
        if i == 0:
            People = People[:-2] + 'L'
            print(People)
        elif People[-i-1] == "R":
            People = People[:-i-2] + 'L' + People[len(People)-i-1:]
            print(People)
            # if Result_count(People) > result:
            result = Result_count(People)
        result_list.append(result)
    print(result_list)
    return result_list


# LRRRLLLRLLRL
test_case = int(input("Please enter the number of test cases: "))
for i in range(0, test_case):
    D_line_better()
