from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'This is the About page'

@app.route('/hello/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
    
    
