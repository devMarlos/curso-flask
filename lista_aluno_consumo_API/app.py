from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

frutas = []
registros = []

api_key= "8e8fcb8c7d00d8c1cc05f028baf4c466"

# Criando a rota principal
@app.route("/", methods=["GET", "POST"])
# Definindo a função que vai ser processado na rota principal.
def principal():
    titulo = 'Lista de Frutas'
    # Validando se a requisição feita utiliza o método POST
    if request.method == "POST":
        # Validando se existe um valor associado a "fruta"
        if request.form.get("fruta"):
            # Adicionando as frutas do input na lista
            frutas.append(request.form.get("fruta"))
            
    return render_template("index.html",titulo=titulo, frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    titulo = 'Diário do Professor'
    # Validando se a requisição feita utiliza o método POST
    if request.method == "POST":
        # Validando se existe valores associados ao 'aluno' e a 'nota'
        if request.form.get('aluno' ) and request.form.get('nota'):
            # Adicionando a chave valor para o dicionário
            registros.append({'aluno': request.form.get('aluno'), 'nota': request.form.get('nota')})
            
    return render_template("sobre.html",titulo=titulo, registros=registros)

@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    titulo = 'Lista de Filmes'
    
    if propriedade == 'populares':
        url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}"
    elif propriedade == 'kids':
        url = f"https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key={api_key}"
    elif propriedade == '2010':
        url = f"https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key={api_key}"
    elif propriedade == 'drama':
        url = f"https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key={api_key}"
    elif propriedade == 'tom_cruise':
        url = f"https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key={api_key}"
  
    # crie uma variável "resposta" que ela vai fazer uma requisição a variável url.
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template('filmes.html', titulo=titulo, filmes=jsondata['results'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,  debug=True)

