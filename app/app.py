from flask import Flask

app = Flask(__name__)

#Pagina principal

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>" 

# Esto imprime tu nombre y edad
@app.route('/user/<name>')   
@app.route('/user/<name>/<int:edad>')   
def user(name = None, edad = None): 
    if edad == None:
        return f"<h1>Bienvenido user {name}</h1>" 
    else:
        return f"<h1>Bienvenido user {name} tienes {edad} años</h1>" 
    
# Esto es una calculadora basica

@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>')
def calculadora(num1,num2,num3,operation):
    if operation == "suma":
        return f" La suma de como resultado: {num1 + num2 + num3}"
    elif operation == "resta":
        return f" La resta da como resultado: {num1 - num2 - num3}"
    elif operation == "multiplicacion":
        return f" La multiplicacion da como resultado: {num1 * num2  *num3}"
    elif operation == "divicion":
        return f" La divicion de como resultado: {num1 / num2 / num3}"
    elif operation == "elevado":
        return f" La elevacion da como resultado: {num1 ** num2 **num3}"
    
        

#Login 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if __name__  == '__main__':
    app.run( debug=True)

