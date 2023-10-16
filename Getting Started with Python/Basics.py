x = 5
print(type(x))

x = "ciao"
print(type(x))


citta = ["Roma", "Napoli", "Milano"]
x, y ,z = citta
print(x, y, z)

y = range(6)
print(y)

#trying split method, a method that can pick an entire text and split it in every array index

lista = "mela,banana,kiwi"
print(lista) #print the whole string
lista = (lista.split(",")) #now every object of this "lista" is located in an array index
print(lista[0]) #print mela
print(lista[1]) #print banana
