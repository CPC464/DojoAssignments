from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
    if __name__=="__main__":
        app.run(debug=True)

@app.route('/success')
def succes():
    return "Yaaaaayyy, Success!!!!"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hellooooo " + name