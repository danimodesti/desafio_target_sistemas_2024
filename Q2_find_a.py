from MyEnum import MyEnum

def find_a():
    my_input = input(f"QUESTÃO 2 - Para sair, digite 0. Para continuar, qualquer outra tecla:  ")
    while True:
        if my_input == MyEnum.SAIR_QUESTAO.value:
            break

        my_str = input("Digite sua string para analisar a ocorrência de letra 'a':  ")

        a_amt = 0
        for c in my_str:
            if c.upper() == 'A':
                a_amt += 1

        print(f"A letra 'a' " + ("não " if a_amt == 0 else "") + f"ocorre e ela aparece {a_amt} vezes na string de entrada.")

        my_input = input("0 para sair, qualquer tecla para continuar ~~\n") 