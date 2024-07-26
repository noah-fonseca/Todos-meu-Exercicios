numero = int(input("Digite um número inteiro que seja positivo: "))

if numero <= 0:
	    print("O número digitado deve ser positivo. Tente novamente.")

else:
	#utilize o loop para fazer uma contagem regressiva
	print("Contagem regressiva começando de", numero)

while numero >0:
	print(numero)
	numero -= 1

print("Fim da contagem regressiva!")