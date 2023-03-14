from flask import Flask, request, jsonify, render_template
import statistics

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Adição
@app.route('/add', methods=['POST'])
def addition():
    content = request.json
    arrayNumbers = content['numbers']
    soma = 0
    for i in range(0, len(arrayNumbers)):
        soma += arrayNumbers[i]

    return jsonify(result=soma)


# Subtração
@app.route('/subtract', methods=['POST'])
def subtraction():
    content = request.json
    numbers = content['numbers']
    return jsonify(result=numbers[0] - numbers[1])


# Multiplicação
@app.route('/multiply', methods=['POST'])
def multiplication():
    content = request.json
    numbers = content['numbers']
    return jsonify(result=numbers[0] * numbers[1])


# Divisão
@app.route('/divide', methods=['POST'])
def division():
    content = request.json
    numbers = content['numbers']

    if numbers[1] == 0:
        return jsonify(error="Divisão por zero não é permitida.")
    else:
        result = numbers[0] / numbers[1]
        return jsonify(result=result)


# Raiz Quadrada
@app.route('/square-root', methods=['POST'])
def square_root():
    content = request.json
    number = content['number']
    result = number ** (1/2)

    return jsonify(result=result)


# Potência
@app.route('/power', methods=['POST'])
def power():
    content = request.json
    number = content['number']
    power = content['power']
    result = number ** power
    return jsonify(result=result)


# Média Aritmética
@app.route('/mean', methods=['POST'])
def mean():
    content = request.json
    numbers = content['numbers']
    numbers = [float(n) for n in numbers]
    result = sum(numbers) / len(numbers)
    return jsonify(result=result)


# Média Harmônica
@app.route('/harmonic-mean', methods=['POST'])
def harmonic_mean():
    content = request.json
    numbers = content['numbers']
    result = len(numbers) / sum(1/n for n in numbers)
    return jsonify(result=result)


# Moda
@app.route('/mode', methods=['POST'])
def mode():
    content = request.json
    numbers = content['numbers']
    result = statistics.mode(numbers)
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
