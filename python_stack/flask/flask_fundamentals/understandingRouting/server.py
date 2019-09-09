from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that the 404 status is set explicitly. I.e. this errorhandler only handles 404 errors
    return "Sorry! No response. Try again"
    
@app.route('/')
def index():
    print("index route visited" + "*"*75)
    return render_template('index.html', test='This message is sent from the server')

@app.route('/page2')
def page2():
    print("page2 route visited" + "*")
    return render_template('page2.html', test='Page 2 also got a message from the server')

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return "Hi "+ name

@app.route('/repeat/<int:number>/<this>')
def repeat(number, this):
    return this*number






if __name__=="__main__":
    app.run(debug=True)