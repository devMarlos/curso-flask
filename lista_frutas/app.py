# from flask import Flask, render_template, request, url_for, redirect

# frutas = []
# titulo = 'Lista de Frutas'
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', titulo=titulo, frutas=frutas)

# @app.route('/autenticar', methods=['POST',])
# def autenticar():
#     if request.form['fruta']:
#         frutas.append(request.form['fruta'])
    
#     return redirect(url_for('index'))

# app.run(host='0.0.0.0', port=8080, debug=True)