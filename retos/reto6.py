edad = int(input("Ingresa tu edad:"))
if edad < 4 and edad >= 0:
    print("Tu entrada es gratis.")
elif edad < 19 and edad > 3:
    print("Debes pagar 5 euros.")
elif edad > 18:
    print("Debes pagar 10 euros.")
else:
    print("Edad invalida.")