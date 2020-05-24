from flask import Flask, render_template, request
from mensagem import contato_empresa

app = Flask(__name__)

@app.route('/')
def quem_somos():
    return render_template("home.html")


@app.route("/contato")
def contate_nos():
	return render_template("contato.html")
    
@app.route("/obrigado", methods=["POST", "GET"])
def obrigado():
    if request.method == "POST":
        try:
            print(request.form)
            name = request.form["name"]
            email = request.form["email"]
            telefone = request.form["telefone"]
            contato_empresa(name, email, telefone)
            return render_template("obrigado.html")
        except:
            return'request deu ruim'
    else:
        return "não entrou no metódo do request certo"


@app.route("/<name>")
def user(name):
	return f"Hello {name}!"



if __name__ == "__main__":
    app.run()