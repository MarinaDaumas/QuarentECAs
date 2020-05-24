from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def quem_somos():
    return render_template("home.html")


@app.route("/contanenos")
def contate_nos():
	return 'home'

@app.route("/obrigado", methods=["POST", "GET"])
def obrigado():
    if request.method == "GET":
        print(request.form)
        user = request.form["name"]
        return f'OBRIGADO {user}'
    else:
        return 'outro'


@app.route("/<name>")
def user(name):
	return f"Hello {name}!"



if __name__ == "__main__":
    app.run()