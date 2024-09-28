# függvény
def beolvas():
    szam = float(input("Kérem adjon meg egy számot!"))
    return szam

#eljárás
def negyedikFeladat():
    #4.	Készíts egy programot, amely beolvas 3 valós számot, majd kiírja őket, mindegyiket egy sorba szóközzel elválasztva!

    szam1 = beolvas()
    szam2 = beolvas()
    szam3 = beolvas()
    # print(szam1)
    # print(type(szam1))
    print(str(szam1)+" "+str(szam2)+" "+str(szam3))
