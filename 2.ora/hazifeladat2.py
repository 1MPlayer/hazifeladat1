def valto(szam,mertek):

    if mertek=="cm":
        print(szam/2.54 ," inch")

    elif mertek=="inch":
        print(szam*2.54 ," cm")

if __name__ =="__main__":
    print("adjon meg egy szamot es egy mertekegszeget (inch/cm)")
    szam=float(input())

    mertek=input()

    valto(szam,mertek)