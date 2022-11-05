def love_song(song:str,ques:tuple):
    num = 0
    song = song.lower()
    for index , q in enumerate(ques):
        l = []
        song1 = song[q[0]:q[1]]
        print(song1)
        for elm in song1:

            num = (alefba[elm])
            print(num)
            l.append(num)
        print(l)
        sl = sum(l)
        print(sl)


alefba= {"a": 1 , "b": 2, "c": 3, "d": 4,"e": 5, "f": 6, "g": 7,"h": 8, "i": 9,
         "j": 10, "k": 11, "l": 12, "m":13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
         "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

love_song("sdegf",[(1,3),(2,5)])