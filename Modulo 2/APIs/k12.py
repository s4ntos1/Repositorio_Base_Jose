from flask import Flask ,render_template


app = Flask(__name__)
@app.route('/login')
def home():
    nome= "jose"
    idade="15"
    return f'{nome} seja bem vindo ao sistema, vc tem {idade} anos certo?'

@app.route('/port1')
def port1():
 return render_template("port1.html")

if __name__=="__main__":
    app.run(debug=True)                                                                                                                                            