from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def quem_somos():
    return render_template("home.html")


@app.route("/contanenos")
def contate_nos():
	return render_template("contato.html")

@app.route("/obrigado", methods=["POST", "GET"])
def obrigado():
    if request.method == "POST":
        try:
            print(request.form)
            user = request.form["name"]
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