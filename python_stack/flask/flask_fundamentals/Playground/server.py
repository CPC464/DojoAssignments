from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that the 404 status is set explicitly. I.e. this errorhandler only handles 404 errors
    return "Sorry! No response. Try again"
    
@app.route('/')
def index():
    print("index route visited" + "*"*75)
    return render_template('index.html', test='This message is sent from the server')
    
@app.route('/play/<number>/<color>')
def play(number, color):
    print("play route visited" + "*"*75)
    number = int(number)
    if (isinstance(number, int) == False):
        return "You did not type an integer. Please try again" 
    else:
        return render_template('play.html', number=number, color=color)
  
        
   
    
@app.route('/page2')
def page2():
    print("page route visited" + "*"*75)
    return render_template('page2.html', test='Page 2 also got a message from the server')







if __name__=="__main__":
    app.run(debug=True)