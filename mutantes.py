from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo!, por favor funciona"

@app.route('/stats', methods=['GET'])
def getStats():
    dic = {"0":"Respuesta Exitosa"}
    return dic

@app.route('/mutans')
def isMutant():
    dic = {"0":"Falta implementar la funcion mutantes"}
    return dic

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=80)
