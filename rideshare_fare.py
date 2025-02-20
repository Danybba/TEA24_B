""" Fahrpreis Mitfahrgelegenheit / Rideshare fare
- Wir verwenden unsere Kenntnisse zu if, elif und else Bedingungen um einen Fahrpreis 
  der Mitfahrgelegenheit abhängig von der Fahrtenart zu kalkulieren. 
  Erstellen Sie die Variablen ride_type. Fragen Sie über die input Funktion vom 
  Nutzer ab ob er ein Fahrtenupgrade plus oder comfort haben möchte. Wir möchten hier 
  den String speichern. 
- Weiter fragen wir den Nutzer ab ob er verfügbare Credits hat. Dieser soll uns die 
  Anzahl seiner credits eingeben, welche wir in einer Variable credits speichern.  
  Wir erstellen eine Variable ride_price und final_price und initialisieren diese 
  mit dem Wert 0. 
- Jetzt prüfen wir ab ob ride_type dem String plus entspricht. Sollte dies der Fall 
  sein, aktualisieren wir ride_price auf 20,5. Sollte dies nicht der Fall sein, 
  prüfen wir ride_type auf comfort ab. Ist das der Fall aktualisieren wir ride_price 
  auf 37,9. Trifft keine der beiden Abfragen zu so wir der Preis ride_price auf 
  18,7 festgelegt.
- Nun geben wir den Fahrpreis auf der Console kommentiert aus. Der String soll hierbei 
  den Inhalt der Variable ride_price beinhalten. Immer wenn die Anzahl der vom Nutzer 
  eingegebenen Credits größer 0 ist, möchten wir eine Verrechnung dieser durchführen, 
  wobei die credits vom ride_price abgezogen und in final_price gespeichert werden. 
- Nun geben wir den finalen Fahrpreis ebenfalls auf der Console kommentiert aus. 
  Der String soll hierbei den Inhalt der Variable final_price beinhalten. 
"""

error = False

# Abfrage des Fahrtenupgrades
ride_type = input("Möchten Sie ein Fahrtenupgrade (plus oder comfort)? ")

# Abfrage der verfügbaren Credits
credits = (input("Wie viele Credits haben Sie? "))

try:
    credits = float(credits)
except:
    print("Bitte geben Sie eine gültige Zahl ein.")
    error = True

# Initialisierung der Variablen
ride_price = 0
final_price = 0

# Überprüfung des Fahrtenupgrades und Festlegung des Fahrpreises
if "plus" == ride_type.lower():
    ride_price = 20.5
elif "comfort" == ride_type:
    ride_price = 37.9
else:
    ride_price = 18.7

# Ausgabe des Fahrpreises
print(f"Der Fahrpreis beträgt: {ride_price} Euro")

# Verrechnung der Credits
if False == error:
    if credits > 0:
        final_price = ride_price - credits
    else:
        final_price = ride_price
else:
    print("Fehler bei der Eingabe der Credits.")

# Ausgabe des finalen Fahrpreises
print(f"Der finale Fahrpreis nach Verrechnung der Credits beträgt: {final_price} Euro")