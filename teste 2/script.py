from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', resultado= 0)

@app.route('/calcula', methods=["POST"])
def calculado():
    valorezinhos = request.form.get('campooculto')
    if valorezinhos:
        try:
            resultado = str(eval(valorezinhos))
            if len(resultado) > 10:
                resultado = resultado[:10]
        except:
            resultado = 'Erro...'
    else:
        resultado = 'Nada aqui'
    return render_template('index.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)