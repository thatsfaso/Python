#annidate while
fila = 1
while fila <= 3:
    posto = 1
    while posto <= 5:
        print("Fila:", fila, "- Posto:", posto)
        posto += 1
    fila += 1

#condition while with even and odds numbers

contatore = 0

while contatore <= 10:
    if contatore % 2 == 0:
        print(contatore, "è pari")
    else:
        print(contatore, "è dispari")
    contatore += 1

#while with break statement
tentativi = 1

while tentativi <= 3:
    password = input("Inserisci la password: ")
    if password == "faso":
        print("Accesso Consentito")
        break
    else:
        print(f"Password errata! \nHai altri {3 - tentativi} tentativi rimasti")
        tentativi += 1

if tentativi > 3:
    print("Hai raggiunto il limite massimo di tentativi!")

