# Author Tihan Morrol (credits to Ael Banyard)
# Berechnung von Renditen anhand von verschiedenem Eigenkapital anhand verschiedener verzinsung des Fremdkapitals
print("============================")
print("Fremdkapital auf 5% verzinst")
print()
ek = [90, 80, 70, 60, 50, 40, 30, 20, 10]
fkzins = 0.05
roi = 0.12

def gewinn(x):
    fk = 100-x
    g = (roi*100)-(fk*fkzins)
    return g

for x in ek:
    ge = gewinn(x)
    roe = ge/x
    print(roe)


print("============================")
print("Fremdkapital auf 10% verzinst")
print()
fkzins = 0.1

for x in ek:
    ge = gewinn(x)
    roe = ge/x
    print(roe)

print("============================")
print("Fremdkapital auf 15% verzinst")
print()
fkzins = 0.15

for x in ek:
    ge = gewinn(x)
    roe = ge / x
    print(roe)

print("============================")
print("Fremdkapital mit Eingabe verzinst")
print()
print("Geben sie den Zinssatz an (ganze Zahl): ")
fkzins = int(input())/100

for x in ek:
    ge = gewinn(x)
    roe = ge / x
    print(roe)