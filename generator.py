def hundred_char(filename: str, size=100):
    try:
        with open(f"{filename}.txt", "r+") as f:
            f.seek(0)
            while True:
                if len(chars := f.read(size)):
                    yield chars
                else:
                    break
    except:
        print("false")


f = open("testies.txt", "w+")
f.write("""kjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdjh;khkjhajdhajshjaksfhkjhajdhajshjaksfhsadasd
kjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf asdF 3sdffhjh;khksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5DFASDFf4 FSAFD3sdfnsdkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdASDhajsksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 2ASasfdff1a5f4 3sdfnsdhjaksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4asdfadfsafsdfsadas 3sdfnsdvksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21sadasdfasdffa5sadfsaf4 3sdfnsdnsdjhf;khkjhajdhajshjaksfhkjhajdhajshjaksfhsdvdsvoja
asdjkkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjakvsfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21sdaasfa5f4 3sdfnsd;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhdfasafsadjdhfhjh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajaksfhssafdvdsvoja
asdjkkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjasfhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjakvdasfsfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvwerqlwerjqwrcnbdlsfg4qf 21a5f4 3sdfnsd;khkjhajasfdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajaksdhasqdqqeqwf
sadasdsa dsad asdwo29138
vqavsdbaadfbsdasjkdjjlaskdjowajdhajshjaksfhkjhajdhajshjaksfhkjhajdhfhjh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjbzbhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajdksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFaeav affkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajbadhajsd cshjaksfhkjhajdhajshjaksfhkjhajdhajdksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HewqwqerFkdhgjk;ha daaavbvljcnbd adf4 3sdfnssadkhdsaQWEkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodjwq HFkdhgjk;hbrvljdfasdfewcnbdlsfg4qf 21a5f4 3sdfnsd""")
f.close()
for i, j in enumerate(hundred_char("testies")):
    print(i, j, "\n")
