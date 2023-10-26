#if annidate
età = 18
documento = True

if età >= 18:
    if documento:
        print("Puoi accedere al locale")
    else:
        print("Devi avere un documento")
else:
    print("Sei minorenne, non puoi accedere")

#shortest vers

if età >= 18 and documento:
    print("Puoi accedere al locale")
else:
    print("Non puoi accedere")


#one line condition

età = 20
maggiorenne = True if età >= 18 else False
print(maggiorenne)


#example
value = 15

if(value > 10 or value < 5) and not value == 12:
    print("Questo numero va bene!")
