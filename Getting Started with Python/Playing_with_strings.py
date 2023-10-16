#con tripli doppi apici puoi scrivere testo multilinea
#RICORDA apice o doppio apice sono la STESSA cosa
testo = """incredibile
questo è 
testo 
multilinea!!"""

print(testo)
print(len(testo))

#stampa di un loop, ovvero lettera per lettera ogni riga
for carattere in "loop":
    print(carattere)

#stampa i primi 3 caratteri di una stringa, oppure altri range, ANCHE NEGATIVI (così parte dal fondo)
print(testo[:3])
print(testo[30:])
print(testo[28:41])

i = " ciao sono Faso "
print(i.strip()) #cancella lo spazio iniziale e finale
i = "ciao sono Faso"
print(i.lower())
print(i.upper())
print(i.replace("o", "i"))

testo = "Ciao sono Iliano, nato il {} Marzo"
print(testo.format(14))
#oppure
x = 14
print(testo.format(x)) #è la stessa cosa


testo = "Ciao sono Iliano, nato il {} Marzo {}"
print(testo.format(14, 2000))
testo = "Ciao sono Iliano, nato il {1} Marzo {0}" #possiamo cambiare gli indici direttamente nella stringa
print(testo.format(14, 2000))

#ESCAPE dei caratteri
testo = 'l\'albero'
print(testo)
testo = "Francesco \"Pio\" Contaldo"
print(testo)
