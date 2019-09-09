from flask import Flask, request, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    print("index route visited" + "*"*75)
    return render_template('index.html', test='This message is sent from the server')

@app.route('/page2')
def page2():
    print("page2 route visited" + "*")
    return render_template('page2.html', test='Page 2 also got a message from the server')





if __name__=="__main__":
    app.run(debug=True)