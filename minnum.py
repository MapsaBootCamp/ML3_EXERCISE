# list1 =[1,2,3,4,5,6,7,8,9]
# def mn(list : list1, num: int):
#     list2 =[]
#     num = 20
#     if num in list1:
#         print(num)
#     else:
#         list2.append(max(list1))
#         print(list2)
#         list1.remove(max(list1))
#         print(list1)
#         list2.append(max(list1))
#         list1.remove(max(list1))
#         # print(list1)
#         # print(list2)
#         num2 = sum(list2)
#         print(num2)
#         list2.sort()
#         print(list2)
#         if num2 == num :
#             print(num2)
#
#         elif num2 < num :
#             list2.append(max(list1))
#             list1.remove(max(list1))
#             num3 = sum(list2)
#             print(num3)
#             if num3 > num :
#                 list2.remove(min(list2))
#                 list2.append(max(list1))
#
#                 print(list2)
num = 45
l1 = 9
l2 =[9]

if num in range(10):
    print(num)
else:

    while sum(l2) < num:

       l1 = l1 - 1
       l2.append(l1)
       sum(l2)


    f = sum(l2) - num

    l2[-1] = l2[-1] - f
    l2.sort()

    for elm in l2:
        print(elm ,  end =" ")



















