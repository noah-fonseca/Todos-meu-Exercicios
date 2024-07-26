# Contagem regressiva:
	
# 	numero = int(input("Digite um número inteiro que seja positivo: "))
# 	if numero <= 0:
# 	    print("O número digitado deve ser positivo. Tente novamente.")
# 	else:
# 	    #utilize o loop para fazer uma contagem regressiva
# 	    print("Contagem regressiva começando de", numero)
# 	    while numero >0:
# 	        print(numero)
# 	        numero -= 1
# 	    print("Fim da contagem regressiva!")

# Recriando uma calculadora:
	
# 	#programa que solicita o número e traz a tabuada desse número de 1 a 10
# 	tabuada = int(input("Digite um número para saber a tabuada do 1 ao 10: "))
# 	for n in range(11):
# 	    numero = [tabuada * n]
# 	    print (tabuada," X ", n, "=", numero)
	
# Somando um número a partir do 1 até o número escolhido:
	
# 	numero = int(input("Digite um valor inteiro para ser somado: "))
# 	soma = 0
# 	for i in range(1, numero + 1):
# 	    soma += i
# 	print (f"A soma dos números de 1 até {numero} é igual a {soma}")
	
# Calculando IMC:
	
# 	#calcular IMC
# 	def calcular_imc(peso, altura):
# 	    imc = peso / (altura ** 2)
# 	    return imc
# 	peso = float(input("Digite o seu peso (kg): "))
# 	altura = float(input("Digite a sua altura (m): "))
# 	imc = calcular_imc(peso, altura)
# 	print("Seu IMC é:", imc)
	
# Verificar se um número é primo ou não:
	
# 	N = int(input("Informe um número para ver se ele é primo: "))
# 	if N <= 1:
# 	    print(f"{N} não é um número primo.")
# 	else:
# 	    primo = True
# 	    for i in range(2, int(N**0.5) + 1):
# 	        primo = False
# 	        break
# 	    if primo:
# 	        print(f"{N} é um número primo.")
# 	    else:
# 	        print(f"{N} não é um número primo.")

# Pedindo a idade do usuário e falando quanto tempo falta para ele chegar aos 100 anos:

# 	nome = input("Digite seu nome: ")
# 	idade = int(input("Digite sua idade: "))
# 	anos_restantes = 100 - idade
# 	print(f"Olá {nome}! Você tem {idade} anos. Você terá 100 anos em {anos_restantes} anos.")
	
# Calculando a área e perímetro de um retângulo: 
	
# 	largura_retangulo = float(input("Digite a largura do retângulo: "))
# 	altura_retangulo = float(input("Digite a altura do retângulo: "))
# 	#calcula a área do retangulo
# 	area = largura_retangulo * altura_retangulo
# 	#calcula o perimetro do retangulo
# 	perimetro = 2 * (largura_retangulo + altura_retangulo)
# 	print(f"A área do retângulo é: {area}.")
# 	print(f"O perimetro do retângulo é: {perimetro}.")
	
# Conversos de temperatura:
	
# 	digite_celsius = float(input("Digite a temperatura em celsius para ser convertida para fahrenheit: "))
# 	#calculo para converter celsius para fahrenheit
# 	fah = (digite_celsius * 9 / 5) + 32
# 	print(f"O Celsius {digite_celsius}°C convertido para Fahrenheit é: {fah}°F ")
# 	digite_fah = float(input("Digite a temperatura em fahrenheit para ser convertida em celsius: "))
# 	#calculo para converter fahrenheit em celsius
# 	celsius = (digite_fah - 32) * 5 / 9
# 	print(f"O Fahrenheit {digite_fah}°F convertido para Celsius é: {celsius}°C ")
	
# Verifica se uma lista de números são par ou impar:
	
# 	numeros = input("Digite uma lista de númros separador por um espaço que deseja conferir se é impar ou par: ")
# 	numeros_lista = [int(numero) for numero in numeros.split()]
# 	for numero in numeros_lista:
# 	    if numero % 2 == 0:
# 	        print(f"O número {numero} é par.")
# 	    else:
# 	        print(f"O número {numero} é impar.")
	
# Soma uma lista de números informados: 
	
# 	numeros = input("Digite uma lista de números para serem somados entre eles: ")
# 	calcular_lista = [float(numero) for numero in numeros.split()]
# 	soma = sum(calcular_lista)
# 	print(f"A soma de todos os números é: {soma}")
	
# 	Código melhorado :
		
# 		numeros = input("Digite uma lista de números para serem somados entre eles: ")
# 		#faz um calculo utilizando os espaços que é a função split para identificar uma lista
# 		calcular_lista = [float(numero) for numero in numeros.split()]
# 		#calcula a soma da lista
# 		soma = sum(calcular_lista)
# 		#calcula a media da soma da lista
# 		media = soma / len(calcular_lista)
# 		#qual o menor numero da lista
# 		menor = min(calcular_lista)
# 		#qual o maior numero da lista
# 		maior = max(calcular_lista)
# 		#printa todas as informações acima
# 		print(f"A soma de todos os números é: {soma}")
# 		print(f"A media de todos os números é: {media}")
# 		print(f"O menor de todos os números é: {menor}")
# 		print(f"O maior de todos os números é: {maior}")
		
	
