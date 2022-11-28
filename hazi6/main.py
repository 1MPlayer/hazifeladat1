def maganhangzo_torles(s):
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzos_s = ""
    for k in s:
        if k not in maganhangzok:
            massalhangzos_s += k
    return massalhangzos_s

lin=[]

with open("hazi.txt","r",encoding='UTF-8') as f:
    with open("hazibe.txt", "w",encoding='utf-8') as w:
        for li in f:
            if li.strip():
                w.write(li)
    with open("hazibe.txt", "r",encoding='utf-8') as d:
        sor=d.readline()
        so=d.readline()
        sorsz=1
        while sor:
            if(sor!="\n"):
                if(sorsz%3==0):
                    print(sor)
                sorsz=sorsz+1
            sor=d.readline()
    with open("hazibe.txt", "r", encoding='utf-8') as c:
        while so:
            if(so!="\n"):
                for line in c:
                    line_word = line.replace(',','').replace('.','').replace('\n','').split(' ')

                    for w in line_word:
                        x=maganhangzo_torles(w)
                        lin.append(x)
            with open("haziki.txt","w",encoding='utf-8')as g:
                g.write(str(lin)+"\n")
            so=c.readline()

