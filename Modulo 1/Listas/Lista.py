tenis = ["nike TN ", "air force 1", "jordan 11","jordan 4", "adidas campo" ]
carrinho = []
opcao = 0
while opcao!=4:
    opcao = int(input(f" oq vc quer fazer: \n1- ver carrinho \n2- ver tenis disponiveis  \n3- adicionar ao carrinho \n4-sair do site: "))
    if opcao ==1:
        print(f"itens do carrinho: \n {carrinho}")
    elif opcao== 2:
        print(f"temos esses \n {tenis}")
    elif opcao ==3:
        adicionar= input(f"qual tenis vc deseja adicionar: \n") 
        carrinho.append(adicionar)
