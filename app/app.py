from flask import Flask

app = Flask(__name__)

#Pagina principal

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>" 

# Esto imprime tu nombre y edad
@app.route('/user/<name>')   
@app.route('/user/<name>/<int:edad>')   
def user(name = None, edad = None): 
    if edad == None:
        return f"<h1>Bienvenido user {name}</h1>" 
    else:
        return f"<h1>Bienvenido user {name} tienes {edad} años</h1>" 
    

        
#Login 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if __name__  == '__main__':
    app.run(debug=True)

