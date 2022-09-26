def fug(mondat):
    import collections
    print(collections.Counter(mondat))
    print(mondat[::-1])
    print(mondat.split())

if __name__=="__main__":
    print("Adjon meg egy mondatot")
    mondat=input()
    fug(mondat)