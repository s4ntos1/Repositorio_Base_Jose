import os
print("Diretório atual:")
print(os.getcwd())
os.mkdir("Projeto1")
print("Pasta criada!")
open("Projetos/matematica.txt", "w").close() 
open("Projetos/portugues.txt", "w").close() 
open("Projetos/ciencias.txt", "w").close()
os.rename("Projetos/portugues.txt", "historia.txt")

arquivos = os.listdir()
for item in arquivos:
     print(item)
     for i in range(1, 4):
      nome = f"relatorio_{i}.txt"
     with open(nome, "w") as arq:
         arq.write("Conteúdo gerado por Python\n")
     print(f"{nome} criado")
if os.path.exists("Projeto/matematica.txt"):
         os.remove("Projetos/matematica.txt")
         print("Arquivo apagado")
else:
     print("Arquivo não encontrado")
