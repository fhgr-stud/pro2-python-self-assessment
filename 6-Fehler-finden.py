# Übung: Fehler finden, Fehlermeldungen verstehen
# ===============================================
# Bearbeiten Sie die folgenden Aufgaben am besten zu zweit - bitte melden Sie sich, wenn Sie Fragen haben - ich komme gerne zu Ihnen!

# Jedes Beispiel enthält einen Fehler. Führen Sie die Beispiele aus und versuchen Sie, die Fehlermeldungen zu verstehen. 
# Korrigiert Sie im Anschluss den Fehler und führen Sie den Code erneut aus, bis keine Fehlermeldungen mehr erscheinen.
# 
# Fehler kommen beim Programmieren oft vor, deshalb ist es wichtig, dass Sie Fehlermeldungen lesen und verstehen können. 
# 
# Wieder andere Code-Abschnitte sind nicht falsch (aus Sicht von Python), aber sie machen nicht das, was Sie wollen. Bitte korrigieren Sie auch diese Beispiele


# Beispiel 1
def gruss(name)
    return f"Hallo, {name}!"

gruss("Max")


# Beispiel 2
fruits = ["Apfel", "Banane", "Kirsche"]
for fruit in fruits
print(fruit)


# Beispiel 3
def verdopple(n):
    ergebnis *= 2
    return ergebnis

verdopple(4)


# Beispiel 4
a = 5
b = "3"

ergebnis = a + b
print(ergebnis)


# Beispiel 5
i = 10
while i > 0:
    print(i)
    i += 1


# Beispiel 6
def addiere(a, b):
    return a + b

ergebnis = addiere(5)
print(ergebnis)


# Beispiel 7
def teile(a, b):
    ergebnis = a / b

teilergebnis = teile(8, 2)
print(teilergebnis)


# Beispiel 8
def dividiere(a, b):
    return a / b

ergebnis = dividiere(5, 0)
print(ergebnis)


# Beispiel 9 
x = 10

def setze_wert():
    x = 5

setze_wert()
print(x)


# Beispiel 10
def multipliziere(a, b):
    return a * b

def quadriere(zahl):
    return multipliziere(zahl)

quadriert = quadriere(4)
print(quadriert)


# Beispiel 11
farben = ["rot", "grün", "blau"]
print(farben[3])


# Beispiel 12
liste_a = [1, 2, 3]
liste_b = 4
resultat = liste_a + liste_b
print(resultat)


# Beispiel 13
tupel = (1, 2, 3)
tupel[1] = 4
