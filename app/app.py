from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>" 

@app.route('/user/<name>')
def user(name):
    return f"<h1>Bienvenido user {name}</h1>" 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if __name__  == '__main__':
    app.run(debug=True)

