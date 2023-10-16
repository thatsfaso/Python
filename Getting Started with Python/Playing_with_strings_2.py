#operazioni con le stringhe
nome = input("Inserisci il tuo nome ")
cognome = input("Inserisci il tuo cognome ")
print(f"ciao {nome.upper()} {cognome.upper()}") #scrive nome e cognome in maiuscolo
print(f"il tuo nome ha {len(nome)} lettere") #conta le lettere nel nome

print(f"Inizia con {nome[0].upper()}")
print(f"e finisce con {nome[-1].upper()}")

print(f"Il tuo cognome al contratio e' {cognome[::-1].lower()}") #backwards print

#alternative
risposta = "Il tuo nome ha {} lettere, inizia con {} e finisce con {}. \n Inoltre il tuo cognome al contrario è {}"
print(risposta.format(len(nome), nome[0].upper(), nome[-1].upper(), cognome[::-1].lower()))

----------------------------------------------------
#textcheck
cognome = input("Inserisci cognome: ")

if cognome == "Fasolino":
    print("Sei Fasolino")
elif cognome.isdigit():
    print("Non inserire solo numeri!")
else:
    print(f"NON sei Fasolino, sei {cognome}")
