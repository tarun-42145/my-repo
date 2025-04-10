from flask import Blueprint, render_template, request

calculator_blueprint = Blueprint('calculator', __name__, template_folder = 'templates')



@calculator_blueprint.route('/')

def home ():
    return render_template('calculator.html')

@calculator_blueprint.route('/calculate', methods = ['POST'] )

def calculate():
    try:

        number_1 = float(request.form['num1'])
        number_2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = number_1 + number_2

        elif operation == 'subtract':
            result = number_1 - number_2
        
        elif operation == 'multiply':
            result = number_1 * number_2
        
        elif operation == "divide":
            if number_2 != 0:
                result = number_1 / number_2
            else:
                result = "Error: Cannot divide by zero"
        
        else:
            result = "Invalid operation"

        return render_template('calculator.html', result=result)
    
    except:
        
        return render_template('index.html', result="Error: Invalid input")
