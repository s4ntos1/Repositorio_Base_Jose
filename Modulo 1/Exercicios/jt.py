def vida_de_jogador():
    nome = input(f"qual seu nome?")
    altura = float(input(f"qual sua altura? "))
    peso = float(input(f"qual seu peso? ")) 
    posicao = input(f"qual posição vc joga: ")
    opcao = int(input(f" de qual país vc é: \n1- Brasil \n2- Portugal :"))
    if opcao == 1:
        opcao1 = int(input(f" qual base vc quer fazer no Brasil: \n1- Goías \n2- Amazonas  \n3- Guaraní \n4- Audax OS:"))
        if opcao1 == 1:
            print(f"bem-vindo ao Goías!, vc é o novo {posicao} do nosso time")
        elif opcao1 == 2:
            print(f" vc escolheu logo o Amazonas mas seja bem-vindo, vc é o novo {posicao} do nosso time")
        elif opcao1 == 3:
            print(f"caramba logo o guaraní, vc é o novo {posicao} do nosso time")
        else:
            print(f"seja bem vindo ao Audax OS, vc é o novo {posicao} do nosso time")
    else:
      opcao2 = int(input(f" qual base vc quer fazer em Portugal: \n1- Benfica \n2- Sporting  \n3- Porto \n4- Braga:"))               
    if opcao2 == 1:
            print(f"bem-vindo ao Benfica!, vc é o novo {posicao} do nosso time")
    elif opcao2 == 2:
            print(f" seja bem-vindo ao Sportting, vc é o novo {posicao} do nosso time")
    elif opcao2 == 3:
            print(f"seja bem-vindo ao Porto, vc é o novo {posicao} do nosso time")
    else:
            print(f"seja bem vindo ao Braga, vc é o novo {posicao} do nosso time")
vida_de_jogador()