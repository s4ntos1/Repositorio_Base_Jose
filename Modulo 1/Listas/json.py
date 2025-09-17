import json
def atividade1():
 dados_json = '{"produto":"Caderno", "preco": 12.5, "estoque": 30}'

 dados_python = json.loads(dados_json)

 print(dados_python["produto"])
 print(dados_python["preco"])

def atividade2():
 aluno ={
 "nome": "Lucas",
 "idade": 16,
 "aprovado": True}
 
 aluno3 = json.dumps(aluno)

 print(aluno3)


def atividade3():
 dados= {
    "filme": "Matrix",
    "ano": 1999,
    "genero": "Ficção Científica"
 }
 modificado =  json.dumps(dados,indent=4)
 print(modificado)
atividade3()
