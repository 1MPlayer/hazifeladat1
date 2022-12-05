class Kutya:
    def __init__(self,nev,kor):
        self.nev=nev
        self._kor=kor

    @property #az ertekvisszateriteshez kell
    def kor(self):
        return self._kor

    @kor.setter
    def kor(self,ertek):
        self._kor=ertek

    def __str__(self):
        return self.nev,"egy ki=utya aki",self._kor*7,"eves!"

    def __eq__(self,masik_kutya):
        return self.nev==masik_kutya.nev and self._kor==masik_kutya._kor

def ugat(nev):
    print(nev,":VAU")

if __name__=="__main__":
    kutyak=[]
    kutyak.append(Kutya("Csibesz",3))
    kutyak.append(Kutya("Zokni", 4))
    kutyak.append(Kutya("Shift", 2))

    print(kutyak[0].nev,kutyak[0].kor)

    if kutyak[1]==kutyak[2]:
        print("A ket kutya egegyezik")

    for i in range(len(kutyak)):
        ugat(kutyak[i].nev)