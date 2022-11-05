# region Solution1
# def _duplicate(t) -> bool:
#     t_array = " ".join(str(t)).split(" ")
#     if len(set(t_array)) != len(t_array):
#         return True
#     return False
#
#
# def digit_sum(t) -> int:
#     t_array = [int(i) for i in " ".join(str(t)).split()]
#     return sum(t_array)
#
#
# n = int(input())
# for i in range(n):
#     s = int(input())
#     t = 0
#     while True:
#         t += 1
#         if _duplicate(t):
#             continue
#         if digit_sum(t) == s:
#             break
#     print(t)
# endregion

# region Solution2
# n = int(input())
# for i in range(n):
#     t = int(input())
#     if t > 45 or t < 1:
#         raise SyntaxError("Not in range (1,45)")
#     if 1 <= t <= 9:
#         print(t, end="")
#     else:
#         number = list()
#         for j in range(9, 0, -1):
#             if t > j:
#                 t -= j
#                 number.append(j)
#             else:
#                 number.append(t)
#                 break
#         number.reverse()
#         for j in number:
#             print(j, end="")
#     print("")
# endregion
