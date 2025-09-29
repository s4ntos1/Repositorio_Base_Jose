import requests
#url =  "https://jsonplaceholder.typicode.com/posts"
#response = requests.get(url) 
#if response.status_code == 200: 
 #print("Aqui estão os usuários!") 
 #print(response.json()) 
#else: 
 #print(f"Opa! Algo deu errado. Status: {response.status_code}") 

#novo_usuario = { 
# "Nome": "robison", 
# "Idade": 14, 
# "Curso": "marketing" 
#} 

#response = requests.post(url, json=novo_usuario) 
 
#if response.status_code == 201: 
# print("Novo usuário criado com sucesso!") 
#else: 
 #print(f"deu erro meu mano. Status: {response.status_code}") 
userId=89
usuario_atualizado={
"userId": 10,
    "id": 99,
    "title": "vladimir put",
     "body":"vanderson"
} 
url =  f"https://jsonplaceholder.typicode.com/posts/{userId}"
#response = requests.put(url, json=usuario_atualizado) 

#if response.status_code == 200: 
 #print("Usuário atualizado com sucesso!") 
 #print(response.json()) 
#else: 
# print(f"Ops! Algo deu errado. Status: {response.status_code}") 
response = requests.delete(url) 
if response.status_code == 200: 
 print(f"Usuário com ID {userId} excluído com sucesso!") 
else: 
 print(f"Erro ao excluir usuário. Status: {response.status_code}") 
