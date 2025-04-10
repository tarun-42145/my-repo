from flask import Flask
from blueprints.calculator import calculator_blueprint

app = Flask(__name__)

app.register_blueprint(calculator_blueprint, url_prefix = '/calculator')

@app.route('/')
def home():
    return 'Welcome to the Calculator App! Visit /calculator for the calculator page.'



if __name__ == '__main__':
    app.run(debug = True)

