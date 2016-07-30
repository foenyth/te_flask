from flask import Flask
# from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="flaskaline"):
    # name = request.args.get('name', name)
    return 'Hello, {}!'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)

app.run(debug=True)
