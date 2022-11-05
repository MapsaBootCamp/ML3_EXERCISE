def validation(k, array):
    array1 = list()
    array2 = list()
    for i in range(1, k + 1):
        index = i - 1
        if index < k // 2 and array[index] == "L":
            array1.append(index)
            array2.append(k - 1 - 2 * index)
        elif index < k // 2 and array[index] == "R":
            array1.append(k - 1 - index)
            array2.append(0)
        elif index >= k // 2 and array[index] == "R":
            array1.append(k - 1 - index)
            array2.append(2 * index - k + 1)
        else:
            array1.append(index)
            array2.append(0)
    return array1, array2


n = int(input())
for i in range(n):
    k = int(input())
    array = " ".join(input()).split(" ")
    array1, array2 = validation(k, array)
    # print(f"{array}  {array1}  {sum(array1)}")
    # print(f"{sum(array1)}", end=" ")
    for j in range(k):
        mx = max(array2)
        if array2 != [0] * k:
            for t in range(j, k):
                if t % 2:
                    index = k - 1 - (t // 2)
                    if array2[index] == mx:
                        array[index], array1[index] = "L", index
                        break
                else:
                    index = t // 2
                    if array2[index] == mx:
                        array[index], array1[index] = "R", k - 1 - index
                        break

        print(f"{sum(array1)}",end=" ")
        array1, array2 = validation(k, array)
    print("")
