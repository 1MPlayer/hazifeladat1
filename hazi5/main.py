elrendezes="{0:>4}{1:>2}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}{13:>4}"

print(elrendezes.format(" "," ","1","2","3","4","5","6","7","8","9","10","11","12"))
print("     :------------------------------------------------")
for i in range(1,13):
    print(elrendezes.format(i,":",i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12),sep='')


def pal(szo):
    rev=szo[::-1]
    if(szo==rev):
        print("A megadott szo palindrom.")
    else:
        print("A megadott szo nem palindrom.")

if __name__=="__main__":
    szo=input(str("Adja meg az ellenorizni kivant szot:"))
    pal(szo)