class Team:
    def __init__(self,nev,projekt,szerepkor):
        self._nev=nev
        self._projekt=projekt
        self._szerepkor=szerepkor
        print("-- Developer letrehozva --")
        print(nev," a ",projekt,"-en dolgozik ",szerepkor,"szerepkorben.")


if __name__=="__main__":
    dol1=Team("Ricsi","SolArch","Frontend")
    dol2=Team("Angela","ZerTeng","Tesztelo")
    dol3=Team("Peti","KefERP","Backend")
    dol4=Team("Eva","KefERP","Frontend")

    print()
    d=[dol1,dol2,dol3,dol4]
    for i in range(0,4):
        for j in range((i+1),4):
            if(d[i]._projekt==d[j]._projekt):
                print(d[i]._nev,"es",d[j]._nev,"dolgoznak egy prijekten.")