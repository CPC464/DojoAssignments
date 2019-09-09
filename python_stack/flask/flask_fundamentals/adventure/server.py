from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', test='This works')

@app.route('/a')
def pagea():  
    return render_template('a.html', test='A works')

@app.route('/a/<name>')
def pageaname(name=""):  
    return render_template('a.html', test='A works', name=name)
    
@app.route('/a1')
def pagea1():
    return render_template('a1.html', test='A1 works')
    
@app.route('/a2')
def pagea2():
    return render_template('a2.html', test='A2 works')

@app.route('/b')
def pageb():
    return render_template('b.html', test='B works')

@app.route('/b1')
def pageb1():
    return render_template('b1.html', test='B1 works')
    
@app.route('/b2')
def pageb2():
    return render_template('b2.html', test='B2 works')


if __name__=="__main__":
    app.run(debug=True)