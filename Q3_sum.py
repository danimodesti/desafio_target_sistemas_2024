def sum():
    print("QUESTÃO 3\n")

    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    print(soma) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12
    print("\nPodemos executar o código e perceber que o valor da" + 
          f" variável soma, ao final, será de {soma}.")