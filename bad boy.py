from math import prod


def furthest(dimensions, location):
    if location["i"] <= dimensions["n"] // 2:
        furthest_row = dimensions["n"] - 1
    else:
        furthest_row = 0
    if location["j"] <= dimensions["m"] // 2:
        furthest_col = dimensions["m"] - 1
    else:
        furthest_col = 0
    return furthest_col + 1, furthest_row + 1


dimensions = dict()
location = dict()
location["i"] -= 1
location["j"] -= 1

first_yoyo = furthest(dimensions, location)
first_yoyo_location = {"i": first_yoyo[0], "j": first_yoyo[1]}
second_yoyo = furthest(dimensions, first_yoyo_location)
print(furthest(first_yoyo, second_yoyo))
