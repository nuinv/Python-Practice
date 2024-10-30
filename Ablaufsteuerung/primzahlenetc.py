#Aufgabe: Schreibe ein Programm, indem der USER zwei Zahlen eingeben muss. 
#zwieschen diesen Zahlen sollen alles PRIMZAHLEN rausgefiltert werden. 
#Diese sollen gefunden und auf der Ausgabe dann angezeigt werden. 

print("Hey unbekannter User :)")

name = input("Wie heißt du?")
print("Schön dich hier zu treffen", name, "!")
print("Dann fangen wir mal an.\nDu nennst mir zwei Zahlen.")
print("Und ich filter dir alle Primzahlen raus.")

#if-elif-else Anweisung:
antwort = input("Klingt es gut oder schlecht?")

if antwort.lower() == "gut":
    print("Alles klar dann geht es jetzt los! :D")
elif antwort.lower() == "schlecht":
    print("Du hast keine andere Wahl..#sorriNOTsorri!\nDann geht es jetzt los!")
else:
    print("Du hast dich nicht für gut oder schlecht entschieden.\nAlso entscheide ich für dich.\nES GEHT LOS!!!")

#Primzahl.. laut Internet ist eine Primzahl nur durch 1 und sich selber teilbar
#Sie hat also genau zwei Teiler.
#Die 1 ist keine Primzahl, weil sie nur einen einzigen Teiler hat, die 1
#Die kleinste Primzahl ist die 2, sie ist auch die einzig gerade Zahl.

#Eingabe der beiden Zahlen durch den User:

print("Nenne mir jetzt zwei Zahlen.")
start_zahl = int(input("Gib die erste Zahl ein: "))
last_zahl = int(input("Und jetzt die zweite Zahl: "))

#Falls eine größere Zahl als erstes eingegeben wird.
if start_zahl > last_zahl:
    start_zahl, last_zahl = last_zahl, start_zahl

#Ausgabe der Zahlen dazwischen:
for zahlen in range(start_zahl, last_zahl):
    print (zahlen)

#kp wie man das berechnen soll


