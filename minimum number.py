def m_v_n(num: int):
    sum = ""
    if num > 0:
        for i in range(9, 0, -1):
            if num - i >= 0:
                num -= i
                sum += f'{i}'
    return sum[::-1]


print(m_v_n(20))
