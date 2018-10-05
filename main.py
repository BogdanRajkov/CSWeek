import numpy as np


class Ucenik:

    def __init__(self, kod):
        kod_delovi = kod.split("/")
        self.sifra = np.fromiter(map(int, kod_delovi[0].split(",")), dtype=np.int)
        self.upisani_smer = kod_delovi[1]
        self.ocene = [np.fromiter(map(int, kod_delovi[2].split(",")), dtype=np.int),
                      np.fromiter(map(int, kod_delovi[3].split(",")), dtype=np.int),
                      np.fromiter(map(int, kod_delovi[4].split(",")), dtype=np.int)]
        self.prosek = np.fromiter(map(np.average, self.ocene), dtype=np.float)
        if kod_delovi[5] == 'v':
            self.vukovac = True
        else:
            self.vukovac = False
        self.matura = list(map(float, kod_delovi[6].split(",")))[:3]
        self.afirmativni_bodovi = list(map(float, kod_delovi[6].split(",")))[3]
        self.takmicenja_bodovi = list(map(float, kod_delovi[6].split(",")))[4]
        self.bodovi = 4 * np.sum(self.prosek) + np.sum(self.matura) + self.afirmativni_bodovi + self.takmicenja_bodovi
        self.lista_zelja = np.array(kod_delovi[7:-1])


def sort_function(x):
    return x.bodovi, x.vukovac, x.takmicenja_bodovi, x.matura


slucaj = 'a'
broj_smerova = 2340
broj_ucenika = 65688
uc_txt = open("ucenici.txt", "r")
smer_txt = open("kvote.txt", "r")
bodovi_txt = open("bodovi.txt", "w")

ucenici = np.empty(broj_ucenika, dtype=Ucenik)
line = uc_txt.readline()
for i in range(broj_ucenika):
    ucenici[i] = Ucenik(line)
    line = uc_txt.readline()

smerovi = np.empty(2340, dtype=object)
line = smer_txt.readline()
for i in range(broj_smerova):
    sifra, kvota = line.split(',')
    smerovi[i] = (sifra, int(kvota))
    line = smer_txt.readline()

print(ucenici[0].sifra)
print(ucenici[0].matura)
print(ucenici[0].bodovi)
if slucaj == 'a':
    ucenici = sorted(ucenici, key=lambda x: x.bodovi, reverse=True)
    for ucenik in ucenici:
        print(ucenik.bodovi)
"""
for ucenik in ucenici:
    try:
        print(ucenik.sifra)
    except AttributeError:
        print(ucenik)
"""