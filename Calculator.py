#------------------------------------------------------------------------------------------------------------------------------------------------
#Defenitions

Zahl1 = 0
Zahl2 = 0
Operator = "+"
Output = 0

#Defenitions
#------------------------------------------------------------------------------------------------------------------------------------------------
#Input

Zahl1Temp = input("Zahl1: ")
try:
  Zahl1 = float(Zahl1Temp)
except:
  print("Bitte geben sie nächstes mal eini gültige Zahl ein")

Zahl2Temp = input("Zahl2: ")
try:
  Zahl2 = float(Zahl2Temp)
except:
  print("Bitte geben sie nächstes mal eini gültige Zahl ein")

Operator = input("Operator (+, -, *, /): ")

#Input
#------------------------------------------------------------------------------------------------------------------------------------------------
#Calcualtor

if Operator == "+":
    Output = Zahl1 + Zahl2
elif Operator == "-":
    Output = Zahl1 - Zahl2
elif Operator == "*":
    Output = Zahl1 * Zahl2
elif Operator == "/":
    Output = Zahl1 / Zahl2
else:
    print("Error in Calculator")

#Calculator
#------------------------------------------------------------------------------------------------------------------------------------------------
#Output

print(f"Das Ergebnis ist: {Output}") 