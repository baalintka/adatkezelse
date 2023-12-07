etelnev=["husleves","paradicsomleves","gyümölcsleves"]
etelar=[1200,1100,2000]
szemelyek=["Béla","Kristóf","Kende","Niki","Arnold"]
szdatum=[1950,2001,2003,2009,2000]

'''most annyi lista van hayn tulajdonsaga az adott etelnek'''
'''de ugy lenne a bes ha 1 listank lenne és 1 etelnek egybe kezelhetnenk a tulajdonsagait'''
'''letrehozunk egy eteltipus ezaz az osztaly altalanos leirasa jelenti'''
'''az osztaly feladata hogy összetartozó adatokat egyben tudjunk kezelni
    egy osztálynak lehetnek tulajdonsagai és lehet viselkedese, a tulajdonságok a változók, ugy hivjuk öket hogy
    adattagok, a viselkedések pedig függvények, tagfüggvény egy osztlynak kötelező eleme a konstruktor!
    feladata az adattagok értékének beállítása // konstruktor: speckó függvény ami lefut amikor létrehozom az osztáylpédányt.
    konkret egyed letrehozasa peldanyositassal
    a konkrét példány az objektum
    
'''
print("Az elso leves ara",etelnev[0],etelar[0])
from Szemely import Szemely
from Etel import Etel

etelek=[]
etel1=Etel("husleves",1200,"leves")
etelek.append(etel1)
etel2=Etel("paradicsomleves",1100,"leves")
etelek.append(etel1)
etel2=Etel("pörkölt",2300,"főétel")
etelek.append(etel1)
print(etel1.nev,etel1.ar,etel1.tipus)
for i in range(0,len(etelek),1):
    print(f"Az {i}. étel: {etelek[i].nev} {etelek[i].ar} {etelek[i].tipus}")

szemelyek=[]
szemely1=Szemely("Béla","1950","01","F")
szemelyek.append(szemely1)
szemely2=Szemely("Kristóf","2001","02","F")
szemelyek.append(szemely2)
szemely3=Szemely("Kende","2003","03","F")
szemelyek.append(szemely3)
szemely4=Szemely("Niki","2009","04","N")
szemelyek.append(szemely4)
szemely5=Szemely("Arnold","2000","05","F")
szemelyek.append(szemely5)
for i in range(0,len(szemelyek)):
    print(f"Az {i+1} személyek: {szemelyek[i].nev} {szemelyek[i].szuldatum} {szemelyek[i].szszam}")
    print(f" {szemelyek[i].nev}nek a kora: {szemelyek[i].kor}")




