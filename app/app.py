from flask import Flask

app = Flask(__name__)

#Pagina principal

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>" 

# Esto imprime tu nombre y edad

@app.route('/user/<name>/<int:edad>')   
def user(name, edad):
    if edad == None:
        return f"<h1>Bienvenido user {name}</h1>" 
    else:
        return f"<h1>Bienvenido user {name} tienes {edad} años</h1>" 
    
# Esto es una calculadora basica

@app.route('/calculadora/<int:num1>/<operation>/<int:num2>')
def operation(num1,num2,operation):
    if operation == "+":
        return f" {num1 + num2}"
    elif operation == "-":
        return f" {num1 - num2}"
    elif operation == "*":
        return f" {num1 * num2}"
    elif operation == "div":
        return f" {num1 // num2}"

#Login 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if __name__  == '__main__':
    app.run( debug=True)

