numeros = input("Digite uma lista de números para serem somados entre eles: ")

#faz um calculo utilizando os espaços que é a função split para identificar uma lista
calcular_lista = [float(numero) for numero in numeros.split()]

#calcula a soma da lista
soma = sum(calcular_lista)

#calcula a media da soma da lista
media = soma / len(calcular_lista)

#qual o menor numero da lista
menor = min(calcular_lista)

#qual o maior numero da lista
maior = max(calcular_lista)

#printa todas as informações acima
print(f"A soma de todos os números é: {soma}")
print(f"A media de todos os números é: {media}")
print(f"O menor de todos os números é: {menor}")
print(f"O maior de todos os números é: {maior}")