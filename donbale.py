for _ in range(int(input("enter how many tests you want: "))):
    m = int(input("enter m: "))
    sequence = input("enter sequence: ")
    sequence_list = [i for i in sequence]
    noghteh_shoroo = int(input("noghte shoroo: "))
    a_len = len(set(sequence_list))
    a = sequence_list[noghteh_shoroo:a_len + noghteh_shoroo]
    print(a_len)
    for i in a:
        print(i, end=" ")
    print()


