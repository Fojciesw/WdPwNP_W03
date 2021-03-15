
C = {"masa":12.01, "z":6}
O = {"masa":16.0, "z":8}
H = {"masa":1.008, "z":1}
uop = {"C":C, "O":O, "H":H}

etanol = {"C":2, "H":6, "O":1}
# etanol = {"C":2, "H":5, "O":1, "H":1} źle, wartość pod indeksem H zostaje nadpisana!

print(etanol)
print(uop["C"]["z"],uop["O"]["masa"]) #result: 6 16.0
print(uop)

#Oblicz masę molową etanolu oraz oblicz ile elektronów ma w sumie ta cząsteczka.
#W tym celu napisz pętlę biegnącą po odpowiednich kluczach słownika etanol i sumującą oddzielnie liczby masowe oraz liczby atomowe.
#Oczekiwane wyniki: suma_m = 46.068, suma_z = 26

suma_m = etanol["C"] * uop ["C"]['masa'] + etanol["H"] * uop ["H"]['masa'] + etanol["O"] * uop ["O"]['masa']
print(suma_m)
suma_z = etanol["C"] * uop ["C"]['z'] + etanol["H"] * uop ["H"]['z'] + etanol["O"] * uop ["O"]['z']
print(suma_z)
