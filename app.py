from flask import Flask, request, jsonify
import statistics


app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>Calculadora</h1>

    <p> Escolha uma das operações e envie o número junto. </p>
    <p> /add?num1=&num2= </p>
    <p> /subtract?num1=&num2= </p>
    <p> /multiply?num1=&num2= </p>
    <p> /divide?num1=&num2= </p>
    <p> /divide?num1=&num2= </p>
    <p> /square-root?num= </p>
    <p> /power?num=&power= </p>
    <p> /mean?numbers=[1,2,3] </p>
    <p> /harmonic-mean?numbers=[1,2,3] </p>
    <p> /mode?numbers=[1,2,3] </p>

    '''


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
@app.route('/mean')
def mean():
    numbers = request.args.getlist('numbers')
    numbers = [float(n) for n in numbers]
    result = sum(numbers) / len(numbers)
    return jsonify(result=result)


# Média Harmônica
@app.route('/harmonic-mean')
def harmonic_mean():
    numbers = request.args.getlist('numbers')
    numbers = [float(n) for n in numbers]
    result = len(numbers) / sum(1/n for n in numbers)
    return jsonify(result=result)


# Moda
@app.route('/mode')
def mode():
    numbers = request.args.getlist('numbers')
    numbers = [float(n) for n in numbers]
    result = statistics.mode(numbers)
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
