import negyedik
def hatosFeladat():
    # 6.	Tárolj el két számot egy-egy változóba! Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat teljes műveleti sorrendben.

    szam1 = int(negyedik.beolvas())
    szam2 = int(negyedik.beolvas())

    print(str(szam1)+"+"+str(szam2)+"="+str(szam1+szam2))
    print(str(szam1) + "-" + str(szam2) + "=" + str(szam1 - szam2))
    print(str(szam1) + "*" + str(szam2) + "=" + str(szam1 * szam2))
    print(str(szam1) + "/" + str(szam2) + "=" + str(szam1 / szam2))
    print(str(szam1) + "mod" + str(szam2) + "=" + str(szam1 % szam2))
    print(str(szam1) + "^" + str(szam2) + "=" + str(szam1 ** szam2))
    print(str(szam2) + "^" + str(szam1) + "=" + str(szam2 ** szam1))



