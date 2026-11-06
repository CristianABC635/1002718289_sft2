from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/raiz-cuadrada/<init:numero>', methods=['GET'])
def raiz_cuadrada(numero):
    resultado = numero**1/2
    return jsonify({
        "numero": numero,
        "resultado": resultado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)