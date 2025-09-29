from flask import Flask

n1= 4
n2=4

app = Flask(__name__)
@app.route('/login')
def home():
    nome= "jose"
    idade="15"
    return f'{nome} seja bem vindo ao sistema, vc tem {idade} anos certo?'

@app.route('/')
def soma():
    soma = n1 + n2 
    divisao = n1 / n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    return f'seu resultado {soma} ,\n seu resultado {divisao},seu resultado {subtracao},seu resultado {multiplicacao}'

if __name__=="__main__":
    app.run(debug=True)