#for example

voti = [19, 28, 27, 30, 22]
totale = 0

for voto in voti:
    totale += voto

media = totale / len(voti)
print("La media di voti è:", media)

#index iteration

parole = ["ciao", "mondo", "python"]
for indice, parola in enumerate(parole):
    print("Indice:", indice, "- Parola:", parola)

#range usage

for numero in range(1,6):
    print(numero)
