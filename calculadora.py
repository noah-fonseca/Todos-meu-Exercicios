#programa que solicita o número e traz a tabuada desse número de 1 a 10

tabuada = int(input("Digite um número para saber a tabuada do 1 ao 10: "))
for n in range(11):
	numero = [tabuada * n]

print (tabuada," X ", n, "=", numero)