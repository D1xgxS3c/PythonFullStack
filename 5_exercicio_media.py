#Escreva um programa onde o usuário digite duas notas e ele mostre a média das duas notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))
resultado = (nota1 + nota2) / 2
print(f"A média das notas é: {resultado:.0f}")