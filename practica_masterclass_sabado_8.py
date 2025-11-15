# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Importar librerias:
import math
import random

math.pi                 #El valor de PI es una comstante
math.factorial(5)       #Factorial de un número
abs(-120)               #Obtener el valor absoluto de un número
random.randint(1, 20)   #Generar un valor aleatorio entre 1 y 20


#----------------------CONDICIONAL IF:--------------------------#
#if condicion:
#   instruccion
#else:
#   instruccion

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
dinero = int(input('Cuánto dinero tienes? '))

if(edad >= 18 and dinero >= 50000):
  print(f'{nombre} Bienvenido')
else:
  print('Prohibida la entrada a menores de edad o con dinero insuficiente')
#----------------------


# Realizar un algoritmo que pregunte si un número es par o impar
num = int(input('Ingrese un número entero: '))

if(num % 2 == 0):
  print('El número ingresado es par')
else:
  print(f'El número {num} no es par')
#----------------------


# Realizar un algoritmo para saber cuál es mayor de tres números ingresados:
# Solicitar al usuario que ingrese tres números:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Determinar cuál es el mayor
if num1 > num2 and num1 > num3:
  mayor = num1
elif num2 > num1 and num2 > num3:
  mayor = num2
else:
  mayor = num3

# Mostrar el resultado
print(f"El número mayor es: {mayor:.0f}")
#----------------------


#----------------------BUCLE WHILE:--------------------------#
# Conteo ascendente
i = 1
while i <= 20:
  print(i)
  i = i + 1

# Conteo descendente
i = 20
while i >= 1:
  print(i)
  i = i - 1
#----------------------


# CALCULADORA:
b = 0
while b == 0:
  print("!!!Bienvenido a la calculadora cientifica¡¡¡")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicar")
  print("4. Salir")
  a = int(input())
  if a == 1:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La suma es {num1+num2}")
  elif a == 2:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La resta es {num1-num2}")
  elif a == 3:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La Multiplicación es {num1*num2}")
  elif a == 4:
    b = 1;
    print("Adios")
  else:
    print("Ingresó un numero errado")
#----------------------


# Tabla de multiplicar
num = int(input('Ingrese un número para ver su tabla de multiplicar: '))
i = 1

while i <= 10:
  print(f'{num} x {i} = {num*i}')
  i = i + 1
#----------------------


# JUEGO DE ADIVINANZA:
numero_secreto = random.randint(1, 100)
intentos = 0
print('Adivina un número entre 1 y 100')

while True:
  numero = int(input('Ingresa un número: '))
  intentos = intentos + 1
  if intentos != 5:
    if numero == numero_secreto:
      print(f'¡Felicidades! Adivinaste el número en {intentos} intentos')
      break
    elif numero < numero_secreto:
      print('Ingresa un número mayor')
    else:
      print('Ingresa un número menor')
  else:
    print('Lo siento, PERDISTE!!!')
    break
#----------------------


# Simulación de un carrito de compra
print ("¡Carro de compra!")
total = 0
while True:
  producto = input("Ingrese el nombre del producto o Salir para terminar: ")
  if producto.lower() == "salir":
    break
  else:
    precio = float(input(f"Ingrese el precio del {producto}: "))
    total = total + precio
print(f"El total a pagar es: {total:.2f} pesos")