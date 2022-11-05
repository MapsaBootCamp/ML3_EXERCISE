def masir(graf: list, rstart, bstart ,red =None, blue = None):
    masir1 = 0
    red = set()
    red.add(rstart)
    blue = set()
    blue.add(bstart)

    for rnext in graf[rstart] - red:

        for bnext in graf[bstart]:

            if red == graf and blue == graf:

                masir1 += 1
            else:
                masir(graf , rnext , bnext,  red , blue)
            return red , blue








































