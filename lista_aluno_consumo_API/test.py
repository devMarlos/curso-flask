import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8e8fcb8c7d00d8c1cc05f028baf4c466"
# crie uma variável "resposta" que ela vai fazer uma requisição a variável url.
resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])