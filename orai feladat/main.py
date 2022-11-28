def prim(a):
    i=2
    pri=1
    while(i<a/2):
       if(a%i==0):
           pri=0
       i=i+1
    if(pri==1):
        print("A szam prim")
    else:
        print("A szam nem prim")

def RPS(p1,p2):
    if(p1==p2):
        print("Draw")
    if(p1=="rock" and p2=="scrissor"):
        print("p1 won")
    elif(p1=="scrissors" and p2=="rock"):
        print("p2 won")
    if(p1=="scrissor" and p2=="paper"):
        print("p1 won")
    elif(p1=="paper" and p2=="scrissor"):
        print("p2 won")
    if(p1=="paper"and p2=="rock"):
        print("p1 won")
    elif(p1=="rock" and p2=="paper"):
        print("p2 won")

def fib(b):
    k=0
    j=1
    l=1
    print(j)
    while(l!=b):
        z=k
        print(k+j)
        k=j
        j=z+j
        l=l+1

def legs(c,co,p):
    cl=c*2
    col=co*4
    pl=p*4
    tl = cl + col + pl
    print(tl)


if __name__=="__main__":

    a=int(input("Az ellenorizni kivant szam:"))
    prim(a)

    p1 = str(input("Player 1 choice (rock/paper/scrissor):"))
    p2 = str(input("Player 2 choice (rock/paper/scrissor):"))
    RPS(p1,p2)

    b=int(input("The total number of fibonacci numbers to generate:"))
    fib(b)

    c=int(input("The total number of cickens:"))
    co=int(input("The total number of cows:"))
    p=int(input("The total number of pigs:"))
    legs(c,co,p)