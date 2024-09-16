print("""BIENVENIDO
Ayudame a preparar una arepa""")
harina = float(input("Cuantas tazas de harina:"))
agua = float(input("Cuantas tazas de agua:"))
sal = (float(input("Cauntas cdtas de sal: "))/16/3)
aceite = (float(input("Cuantas cdas de aceite: "))/16)
bol = harina + agua + sal 
budare = bol + aceite 
print("El volumen de tu arepa es ", budare )
