# input() siempre retorna un string
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura (m)? "))

# f-strings: formateo moderno y legible
print(f"Hola {nombre}, tienes {edad} años y mides {altura}m.")