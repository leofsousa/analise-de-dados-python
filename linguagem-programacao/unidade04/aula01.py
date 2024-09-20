from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bem Vindo ao back-end simples com flask'

if __name__ == '__main__':
    app.run(host='localhost', port = 5000)
