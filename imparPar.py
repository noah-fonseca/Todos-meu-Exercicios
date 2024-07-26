numeros = input("Digite uma lista de númros separador por um espaço que deseja conferir se é impar ou par: ")

numeros_lista = [int(numero) for numero in numeros.split()]
for numero in numeros_lista:
	if numero % 2 == 0:
		print(f"O número {numero} é par.")

	else:
		print(f"O número {numero} é impar.")