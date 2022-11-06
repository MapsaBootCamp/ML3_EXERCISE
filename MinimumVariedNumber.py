# https://codeforces.com/problemset/problem/1714/C
def Minimum_Value() -> int:
    number = int(input("Please enter a number:"))
    reversed_result: int = 0
    result = 0
# az 9 shoroo mikone be kam kardan az number va baad reverse mikone
    for i in reversed(range(0, 10)):
        if number > 9:
            number = number - i
            if number > 0:
                reversed_result = reversed_result * 10 + i
            elif number < 0:
                number = number + i
            elif number == 0:
                break
        else:
            reversed_result = reversed_result * 10 + number
            break

    while reversed_result > 0:
        temp = reversed_result % 10
        result = result * 10 + temp
        reversed_result = (reversed_result-temp) / 10
    result = int(result)
    print(result)
    return result


test_case = int(input("Please enter the number of test cases: "))
for i in range(0, test_case):
    Minimum_Value()
