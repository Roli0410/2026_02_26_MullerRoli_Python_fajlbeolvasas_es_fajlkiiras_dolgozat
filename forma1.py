"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

versenyzok= []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        versenyzo = {'név': adatok[0], 'csapat': adatok[1], 'győzelmek_száma': int(adatok[2]), "teljesített_futamok_száma" : int(adatok[3]) }
        versenyzok.append(versenyzo)

# print(forma1_versenyzok)

#1. feladat
versenyzok_szama = len(versenyzok)

# 2. feladat
legtobb_futamgyozelem = versenyzok[0] 
for versenyzo in versenyzok: 
    if versenyzo["győzelmek_száma"] > legtobb_futamgyozelem["győzelmek_száma"]: 
        legtobb_futamgyozelem = versenyzo

# 3. feladat
legkevesebb_futamgyozelem= versenyzok[0]
for versenyzo in versenyzok: 
    while  versenyzo["győzelmek_száma"] < legkevesebb_futamgyozelem["győzelmek_száma"]: 
        legkevesebb_futamgyozelem = versenyzo

# 4. feladat
legtobb_futam = versenyzok[0]
for versenyzo in versenyzok: 
    if versenyzo["teljesített_futamok_száma"] > legtobb_futam["teljesített_futamok_száma"]: 
        legtobb_futam = versenyzo

# 5. feladat
osszes_futam = 0
for versenyzo in versenyzok: 
    osszes_futam += versenyzo["teljesített_futamok_száma"]
atlag = osszes_futam / len(versenyzok)


# 6. feladat
# csapatok_gyozelme = {}
# for versenyzo in versenyzok: 
#     csapat = versenyzo["csapat"]
#     gyozelmek = versenyzo["győzelmek_száma"]

#     if csapat in csapatok_gyozelme:
#         gyozelmek += csapatok_gyozelme
#     else: 
#         gyozelmek = csapatok_gyozelme
# legtobb_csapat = ""
# legtobb_gyozelem = 0

# for csapat, gyozelem in csapatok_gyozelme.items():
#     if gyozelem > legtobb_gyozelem:
#         legtobb_csapat = csapat
#         legtobb_gyozelem = gyozelem

# sajnos nem sikerült

print(f"1. A beolvasott fájlban összesen {versenyzok_szama} versenyző szerepel.")
print(f"2. A legtöbb futamot nyert versenyző: {legtobb_futamgyozelem ["név"]}")
print(f"3. A legkevesebb futamot nyert versenyző: {legkevesebb_futamgyozelem ["név"]  }")
print(f"4. A legtöbb futamot teljesített versenyző: {legtobb_futam ["név"]}")
print(f"5. Az átlagos futamszám: {round(atlag, 2)}")
# print(f"6. A legtöbb futamgyőzelmet szerző csapat: {legtobb_csapat}")