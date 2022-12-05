ze=[]
def beolvas():
    ze=[]

    with open("playlist.txt","r",encoding="utf-8") as f:
        sor=f.readline()
        while sor:
            zene = {}
            zene["eloado"]=sor.split(";")[0]
            zene["cim"] = sor.split(";")[1]
            zene["mufaj"] = sor.split(";")[2]
            zene["hosz"] =int( sor.split(";")[3])
            ze.append(zene)
            sor=f.readline()
        return ze


def teljes_hossz(ze):
    hosz=0
    for i in range(len(ze)):
        hosz+=ze[i]["hosz"]
    perc=hosz//60
    mp=hosz%60
    with open("02_hossz.txt","w",encoding="utf-8") as g:
        g.write("A lejatszasi lista hossza: ")
        g.write(str(perc) +":" +str(mp))

def leghosszabb_rockzene(ze):
    lh=0
    ci=""
    for i in range(len(ze)):
        if(ze[i]["mufaj"]=="rock" and lh<ze[i]["hosz"]):
            lh=ze[i]["hosz"]
            ci=ze[i]["cim"]
    with open("03_leghosszabb_rock.txt","w",encoding="utf-8") as g:
        g.write("A leghosszab rock szam: "+ str(ci))

def leggyakoribb_mufaj(ze):
    mf=[]
    lgmf=0
    lgmn=""
    for i in range(len(ze)):
        mf.append(ze[i]["mufaj"])
    for i in range(0,len(mf)):
        count=1;
        for j in range(i+1,len(mf)):
            if(mf[i]==mf[j]):
                count+=1
        if(count>lgmf):
            lgmf=count
            lgmn=mf[i]
    lgmn=lgmn.upper()
    with open("04_kedvenc_mufaj.txt","w",encoding="utf-8") as g:
        g.write("A kedvenc mufaj: "+ str(lgmn))


ze=beolvas()
beolvas()
teljes_hossz(ze)
leghosszabb_rockzene(ze)
leggyakoribb_mufaj(ze)