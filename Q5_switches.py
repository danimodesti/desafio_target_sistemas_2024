def switches():
    print("QUESTÃO 5\n")
    print("""
        Na sala dos interruptores, sejam eles A, B, C:
          - deixe A ligado por um tempo razóavel (alguns minutos), então
          desligue-o.
          - ligue B.
          - C permanece desligado.

        Na primeira sala, analise:
          - Lâmpada desligada e quente? Então, o interruptor A liga esta lâmpada;
          - Lâmpada acesa? Então, o interruptor B liga esta lâmpada;
          - Lâmpada desligada e fria? Então, o interruptor C liga esta lâmpada.
        
        Com isto, você obtém uma resposta e elimina um interruptor e uma sala.
        Para a segunda ida, basta deixar um interruptor ligado e o outro
        desligado, dentre os que não interagiam com a primeira sala. Assim, 
        ao verificar a segunda sala, analise a situação da sua lâmpada. 
        
        Exemplo:
        digamos que você descobriu que a primeira sala interagia com o interruptor
        A, então você escolhe agora ligar B e deixar C desligado. Se a segunda
        sala estiver com a luz acesa, então seu interruptor é B; caso contrário,
        é C. Por eliminação, você descobre o interruptor da terceira sala.
    """)