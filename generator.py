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
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdffhjh;khksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajsksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdhjaksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdvksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdnsdjh;khkjhajdhajshjaksfhkjhajdhajshjaksfhsdvdsvoja
asdjkkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjakvsfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsd;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhfhjh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajaksfhsdvdsvoja
asdjkkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjaksfhjhfhjh;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajshjakvsfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsd;khkjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajaksdhasd
sadasdsa dsad asdwo29138
asdasdasjkdjjlaskdjowajdhajshjaksfhkjhajdhajshjaksfhkjhajdhfhjh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajdksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsdh;khkvjhajdhajshjaksfhkjhajdhajshjaksfh
kjdhvsjdhvkjhajdhajshjaksfhkjhajdhajshjaksfhkjhajdhajdksfhjh;khkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbd adf4 3sdfnssadkhdsaQWEkjhajdhajshjaksfhkjhaadwueyqouie
acscsjv vJodj HFkdhgjk;hbvljcnbdlsfg4qf 21a5f4 3sdfnsd""")
f.close()
for i, j in enumerate(hundred_char("testies")):
    print(i, j, "\n")
