digite_celsius = float(input("Digite a temperatura em celsius para ser convertida para fahrenheit: "))

#calculo para converter celsius para fahrenheit
fah = (digite_celsius * 9 / 5) + 32

print(f"O Celsius {digite_celsius}°C convertido para Fahrenheit é: {fah}°F ")

digite_fah = float(input("Digite a temperatura em fahrenheit para ser convertida em celsius: "))

#calculo para converter fahrenheit em celsius
celsius = (digite_fah - 32) * 5 / 9

print(f"O Fahrenheit {digite_fah}°F convertido para Celsius é: {celsius}°C ")