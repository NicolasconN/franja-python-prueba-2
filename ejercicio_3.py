from math import pi

radio_circulo = float(input('Escriba el radio del circulo: '))
altura_cilindro = float(input('Escriba la altura del cilindro: '))
radio_cilindro = float(input('Escriba el radio del cilindro: '))

area_circulo = (pi * pow(radio_circulo,2))
volumen_cilindro = (area * altura_cilindro)

print('El area del circulo es: ', area_circulo)
print('El volumen del cilindro es: ', volumen_cilindro)
