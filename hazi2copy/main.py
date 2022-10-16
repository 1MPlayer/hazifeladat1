def szerk(a,b,c):
    if(a+b>c and a+c>b and c+b>a):
        print("A(z) ",a,", ",b,"es",c,"oldalu haromszog szerkesztheto")
    else:
        print("A(z) ",a,", ",b,"es",c,"oldalu haromszog NEM szerkesztheto")

if __name__=="__main__":
    print("Adja meg a haromszog harom oldalat cm-ben")
    a=int(input("a oldal (cm):"))
    b=int(input("b oldal (cm):"))
    c=int(input("c oldal (cm):"))

    szerk(a,b,c)
