
while True:
    real = float(input("Quanto você tem na carteira? "))
    dolar = real / 5.53
    if real == -1:
        break
    print(f"Com R${real:.2f} reais você comprar US${dolar:.2f} dolares.")
print("Fim do seu programa")