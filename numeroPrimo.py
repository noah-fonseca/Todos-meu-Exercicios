N = int(input("Informe um número para ver se ele é primo: "))

if N <= 1:
	print(f"{N} não é um número primo.")

else:
	primo = True

	for i in range(2, int(N**0.5) + 1):
		primo = False

		break

	if primo:
		print(f"{N} é um número primo.")

	else:
		print(f"{N} não é um número primo.")