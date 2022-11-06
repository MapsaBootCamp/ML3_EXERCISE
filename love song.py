def l_s(n: str):
    q = range(int(input()), int(input()))
    for char in n:
        if ord(char) - 96 in q:
            tedad = ord(char) - 96
            print(tedad * char, end="")
        else:
            print(char, end="")


print(l_s("abcdefgh"))
