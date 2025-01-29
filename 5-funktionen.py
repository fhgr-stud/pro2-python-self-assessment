# Übung: Funktionen in Python
# ===========================
# Bearbeiten Sie die folgenden Aufgaben am besten zu zweit - bitte melden Sie sich, wenn Sie Fragen haben - ich komme gerne zu Ihnen!


# Schritt 1
# ---------
# Definieren Sie eine Funktion hallo(), die den Satz "Hallo, Python!" ausgibt, wenn sie aufgerufen wird.
# Rufen Sie die Funktion auf, um sicherzustellen, dass sie funktioniert.


# Schritt 2
# ---------
# Definieren Sie eine Funktion begruesse(name), die einen Namen als Parameter entgegennimmt und "Hallo, [name]!" ausgibt. (Ersetzen Sie [name] durch den übergebenen Namen.)
# Rufen Sie die Funktion mit einem Namen als Argument auf.


# Schritt 3
# ---------
# Erstellen Sie eine Funktion addiere(zahl1, zahl2), die zwei Zahlen als Parameter entgegennimmt, ihre Summe berechnet und diese zurückgibt.
# Rufen Sie die Funktion mit zwei beliebigen Zahlen auf und gib das Ergebnis aus.
# 
# Wichtig: Die Funktion soll die Summe zurückgeben, nicht ausgeben!


# Schritt 4
# ---------
# Definieren Sie eine Funktion operationen(zahl1, zahl2), die zwei Zahlen entgegennimmt und ihre Summe, Differenz, Produkt und Quotient als vier Werte zurückgibt.
# 
# Rufe die Funktion auf und speichere die Rückgabewerte in vier separaten Variablen. Gib diese dann aus.


# Schritt 5
# ---------
# Erstellen Sie eine Funktion potenzieren(basis, exponent=2), die eine Zahl potenziert. Falls kein Exponent übergeben wird, sollte die Zahl standardmäßig quadriert werden.
# Rufen Sie die Funktion einmal mit zwei Argumenten und einmal nur mit einer Basis auf.
# 
# Die folgenden Tests können genutzt werden, um die Funktion zu prüfen:
#    assert(potenzieren(3, 2) == 9)
#    assert(potenzieren(2, 3) == 8)
#    assert(potenzieren(2, 0) == 1)
#    assert(potenzieren(0, 2) == 0)
#    assert(potenzieren(5) == 25)
#    assert(potenzieren(2,8) == 256)


# Schritt 5
# ---------
# Schreiben Sie eine Funktion ist_primzahl(n), die überprüft, ob eine übergebene Zahl n eine Primzahl ist und dementsprechend True oder False zurückgibt.
# Verwenden Sie diese Funktion in einer Schleife, um alle Primzahlen zwischen 2 und 50 auszugeben.


# Schritt 6
# ---------
# Entwicklen Sie eine Funktion zeit_umrechnen(wert, starteinheit, zieleinheit).
#
# Mögliche Werte für starteinheit und zieleinheit sind: 'sekunden', 'minuten', 'stunden'.
# - Die Funktion sollte den wert von der starteinheit in die zieleinheit umrechnen.
# - Die Funktion sollte den umgerechneten Wert zurückgeben.
# - Prüfen Sie ebenfalls ob starteinheit und zieleinheit gültige einheiten sind.
# 


# Die folgenden Tests können genutzt werden, um die Funktion zu prüfen:
#    print(zeit_umrechnen(30, "seunden", "inuten")) # ergibt "Falsche Einheit angegeben"
#    print(zeit_umrechnen(30, "sekunden", "minuten")) # ergibt 0.5
#    print(zeit_umrechnen(1, "minuten", "sekunden")) # ergibt 60.0
#    print(zeit_umrechnen(15, "minuten", "stunden")) # ergibt 0.25
#    print(zeit_umrechnen(1, "stunden", "minuten")) # ergibt 60.0
#    print(zeit_umrechnen(1, "stunden", "sekunden")) # ergibt 3600.0
#    print(zeit_umrechnen(7200, "sekunden", "stunden")) # ergibt 2.0
