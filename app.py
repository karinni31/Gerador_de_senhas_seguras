from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def gerar_senha(opcoes, tamanho):

    caracteres = ""

    if opcoes.get("minusculas"):

        caracteres += string.ascii_lowercase

    if opcoes.get("maiusculas"):

        caracteres += string.ascii_uppercase

    if opcoes.get("numeros"):

        caracteres += string.digits

    if opcoes.get("especiais"):

        caracteres += "!@#$%&*"

    if not caracteres:

        return ""

    return "".join(random.choice(caracteres) for _ in range(tamanho))


@app.route("/")

def home():

    return render_template("index.html")


@app.route("/gerar", methods=["POST"])

def gerar():

    dados = request.json

    senha = gerar_senha({

        "minusculas": dados.get("minusculas"),

        "maiusculas": dados.get("maiusculas"),

        "numeros": dados.get("numeros"),

        "especiais": dados.get("especiais"),

    }, int(dados.get("tamanho", 12)))

    return jsonify({"senha": senha})


if __name__ == "__main__":

    app.run(debug=True)