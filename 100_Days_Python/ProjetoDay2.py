print("Bem-vindo a calculadora de gorjetas")
conta = float(input("Quanto foi o total da conta? "))
corjeta = int(input("Quanto de gorjeta gostaria de dar? 10,12 ou 15? "))
pessoas = int(input("Quantas pessoas irão pagar a conta? "))
total = (conta + (conta * corjeta / 100)) / pessoas

print(f"Cada pessoa irá pagar {round(total,2)}")
