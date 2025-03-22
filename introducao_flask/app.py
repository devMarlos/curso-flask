from flask import Flask, render_template, request

app = Flask('OLA_FLASK')

frutas = []
registros = []

# Criando a rota principal
@app.route("/", methods=["GET", "POST"])
# Definindo a função que vai ser processado na rota principal.
def principal():
    # Validando se a requisição feita utiliza o método POST
    if request.method == "POST":
        # Validando se existe um valor associado a "fruta"
        if request.form.get("fruta"):
            # Adicionando as frutas do input na lista
            frutas.append(request.form.get("fruta"))
            
    return render_template("index.html",frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # Validando se a requisição feita utiliza o método POST
    if request.method == "POST":
        # Validando se existe valores associados ao 'aluno' e a 'nota'
        if request.form.get('aluno' ) and request.form.get('nota'):
            # Adicionando a chave valor para o dicionário
            registros.append({'aluno': request.form.get('aluno'), 'nota': request.form.get('nota')})
            
    return render_template("sobre.html", registros=registros)

app.run(host='0.0.0.0', port=8080,  debug=True)

