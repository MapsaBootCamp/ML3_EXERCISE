def line(n: int):
    for i in range(n):
        m = input("enter L or R")
        sum = 0
        for num, elm in enumerate(m):
            if elm == "r":
                sum += len(m) - (num + 1)
            elif elm == "l":
                sum += num
        return sum
    else:
        print("error")


print(line(5))
