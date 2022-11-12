n = int(input())
s = int(input())
a = int(input())
if s > a:
    pardakht = s / n
    hazine_madarkharj = s + a * (n - 1)
    hazine_afrad = hazine_madarkharj / n - a
    if pardakht % n > 0:
        print(hazine_afrad)
    else:
        print(-1)
else:
    print(-1)
