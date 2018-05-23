# primzahlen überprüfen

zahl = input("Bitte geben Sie die Zahl ein")
zahlI = int(zahl)
prime = False

for i in range (2,zahlI):
    #ist die Zahl durch i teilbar?
    #dann ist es keine Primzahl
    if(zahlI%i == 0):
        prime = True   

    #ist die Zahl nie durch i teilbar?
    #dann ist sie eine Primzahl
if(prime):
    print(zahlI, " ist keine Primzahl")

else:
    print(zahlI, " ist eine Primzahl")
