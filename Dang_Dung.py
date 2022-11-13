# https://quera.org/contest/assignments/45359/problems/156043
# sahm har kas : s/n - s/(n*n) + a - (a/n) + s/n
def Dong():
    number_of_people, restaurant, transaction = input(
        "Please Enter N,S,a (number of people, restaurant and trasaction: ").split(" ")
    number_of_people = int(number_of_people)
    restaurant = int(restaurant)
    transaction = int(transaction)
    result = (((((restaurant/number_of_people) + transaction) *
                (number_of_people - 1)) + (restaurant / number_of_people))/number_of_people) - transaction
    if result.is_integer() == True and result > 0:
        return result

    else:
        return -1


test = int(input("plean enter the number of testcases:"))
for i in range(0, test):
    print(Dong())
