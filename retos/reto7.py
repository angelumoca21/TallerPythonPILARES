tipoPizza = input("""Bienvenido a la pizzeria Bella Napoli
Escoge el tipo de pizza que quieres:
1.Vegetariana
2.No vegetariana\n""")
if tipoPizza == "1":
    ingrediente = input("""Los ingredientes vegetarianos son:
    a.Pimiento
    b.Tofu\n""")
    if ingrediente == "a":
        print("La pizza ordenanda es vegetariana con pimiento, mozarella y tomate.")
    elif ingrediente == "b":
        print("La pizza ordenanda es vegetariana con tofu, mozarella y tomate.")
    else:
        print("Opcion no valida.")
elif tipoPizza == "2":
    ingrediente = input("""Los ingredientes no vegetarianos son:
    a.Peperoni
    b.Jamon
    c.Salmon\n""")
    if ingrediente == "a":
        print("La pizza ordenanda es no vegetariana con peperoni, mozarella y tomate.")
    elif ingrediente == "b":
        print("La pizza ordenanda es no vegetariana con jamon, mozarella y tomate.")
    elif ingrediente == "c":
        print("La pizza ordenanda es no vegetariana con salmon, mozarella y tomate.")
    else:
        print("Opcion no valida.")
