from MyEnum import MyEnum

from Q1_belongs_to_fibo import belongs_to_fibonacci
from Q2_find_a import find_a
from Q3_sum import sum
from Q4_logic_statements import logic_statements
from Q5_switches import switches

def main():
    print("Olá, meu nome é Danielle e este é o meu teste técnico para a Target Sistemas!\n")

    question = None
    while question != MyEnum.SAIR.value:
        try:
            question = int(input("\n\nEscolha uma das perguntas para ver as respostas, ou 0 para sair:  "))
        except ValueError:
            print("Pergunta inválida. Tente de novo.\n")
            continue

        if question == MyEnum.PERGUNTA_1.value:
            belongs_to_fibonacci()
        elif question == MyEnum.PERGUNTA_2.value:
            find_a()
        elif question == MyEnum.PERGUNTA_3.value:
            sum()
        elif question == MyEnum.PERGUNTA_4.value:
            logic_statements()
        elif question == MyEnum.PERGUNTA_5.value:
            switches()
        elif question == MyEnum.SAIR.value:
            print("OK, obrigada por executar meu programa :)")
            break
        else:
            print("Pergunta inválida. Tente de novo.\n")

if __name__ == "__main__":
    main()