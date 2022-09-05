# Author Tihan Morrol (credits to Ael Banyard)
# Berechnung von Renditen anhand von verschiedenem Eigenkapital anhand verschiedener verzinsung des Fremdkapitals

ek = [90, 80, 70, 60, 50, 40, 30, 20, 10]
roi = 0.12

def gewinn(x):
    fk = 100-x
    g = (roi*100)-(fk*fkzins)
    return g

def roeCalc():
    for x in ek:
        ge = gewinn(x)
        roe = ge/x
        print("Bei Gewinn: "+str(ge) +", ist RoE: " + str(roe))

print("============================")
print("Fremdkapital auf 5% verzinst")
print()
fkzins = 0.05

roeCalc()


print("============================")
print("Fremdkapital auf 10% verzinst")
print()
fkzins = 0.1

roeCalc()

print("============================")
print("Fremdkapital auf 15% verzinst")
print()
fkzins = 0.15

roeCalc()

print("============================")
print("Fremdkapital mit Eingabe verzinst")
print()
print("Geben sie den Zinssatz an (ganze Zahl): ")
fkzins = int(input())/100

roeCalc()