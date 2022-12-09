print('Add meg a pizza adatait! ')
sajtos_pizza = 1000
gombas_pizza = 1100
sonkas_pizza = 1200
feltet_ar = 50
csillag = "*" * 20
pizzak = []
meretek = []
feltetek = []

def rendelo():
    rendeles = input("Akar új rendelést rögzíteni? i/n: ")
    while rendeles != "n":
        if rendeles == "i":
            print(csillag)
            print("*1 - sajtos        *")
            print("*2 - gombás        *")
            print("*3 - sonkás        *")
            print(csillag)
            pizza = int(input("Válasszon pizzát: "))
            print(csillag)
            print("*1 - kicsi         *")
            print("*2 - normál        *")
            print("*3 - nagy          *")
            print(csillag)
            meret = int(input("Válasszon méretet: "))
            feltet = input("Kér extra feltétet? i/n: ")
            pizzak.append(pizza)
            meretek.append(meret)
            feltetek.append(feltet)
            print(pizzak)

        rendeles = input("Akar új rendelést rögzíteni? i/n: ")


def szamlalas():
    print(pizzak)
    i = 0
    sajtos_db = 0
    gombas_db = 0
    sonkas_db = 0
    legtobb = 0
    legtobb_fogyott = ""
    while i < len(pizzak):
        if pizzak[i] == 1:
            sajtos_db += 1
        elif pizzak[i] == 2:
            gombas_db += 1
        elif pizzak[i] == 3:
            sonkas_db += 1
        i += 1
    print(f"Ennyi sajtos fogyott: {sajtos_db}")
    print(f"Ennyi gombás fogyott: {gombas_db}")
    print(f"Ennyi sonkás fogyott: {sonkas_db}")
    if legtobb < sonkas_db:
        legtobb_fogyott = "sonkás"
    elif legtobb < gombas_db:
        legtobb_fogyott = "gombás"
    elif legtobb < sajtos_db:
        legtobb_fogyott = "sajtos"

    print(f"Ebből fogyott a legtöbb: {legtobb_fogyott}")

def bevetel():
    osszeg = 0
    ar = 0
    i = 0
    while i < len(pizzak):
        if pizzak[i] == 1:
            ar = sajtos_pizza
            if meretek[i] == 1:
                osszeg += ar * 0.9
            elif meretek[i] == 2:
                osszeg += ar
            elif meretek[i] == 3:
                osszeg += ar * 1.1
        elif pizzak[i] == 2:
            ar = gombas_pizza
            if meretek[i] == 1:
                osszeg += ar * 0.9
            elif meretek[i] == 2:
                osszeg += ar
            elif meretek[i] == 3:
                osszeg += ar * 1.1
        elif pizzak[i] == 3:
            ar = sajtos_pizza
            if meretek[i] == 1:
                osszeg += ar * 0.9
            elif meretek[i] == 2:
                osszeg += ar
            elif meretek[i] == 3:
                osszeg += ar * 1.1
        if feltetek[i] == "i":
            osszeg += 50
        i += 1


    print(f"Ekkora volt a bevétel: {osszeg}")

def feltet_db():
    i = 0
    f_db = 0
    while i < len(feltetek):
        if feltetek[i] == "i":
            f_db += 1
        i += 1
    print(f"Ennyiszer kértek feltétet: {f_db}")

def meret_db():
    i = 0
    kicsi = 0
    normal = 0
    nagy = 0
    legtobb_db = 0
    legtobb = ""
    while i < len(meretek):
        if meretek[i] == 1:
            kicsi += 1
        elif meretek[i] == 2:
            normal += 1
        elif meretek[i] == 3:
            nagy += 1
        i += 1
    if legtobb_db < kicsi:
        legtobb = "kicsi"
    elif legtobb_db < normal:
        legtobb = "normal"
    elif legtobb_db < nagy:
        legtobb = "nagy"

    print(f"Ebből a méretből rendeltek a legtöbbet: {legtobb}")
