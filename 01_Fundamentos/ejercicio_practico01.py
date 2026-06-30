# Ejemplo Practico: Calculadora de Descuento
precio_original = 100.0
descuento = .020
tiene_cupon = True

precio_final = precio_original * (1 - descuento)
aplica_descuento_extra = (precio_final > 50) and tiene_cupon

print(f"Precio final: ${precio_final:.2f}")
print(f"aplica descuento extra? {aplica_descuento_extra}")

