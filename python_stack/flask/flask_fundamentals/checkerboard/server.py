from flask import Flask, request, render_template, redirect, url_for
import random
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that the 404 status is set explicitly. I.e. this errorhandler only handles 404 errors
    return "Sorry! No response. Try again"
    
@app.route('/')
def index():
    print("index route visited" + "*"*75)
    return render_template('index.html', test='This message is sent from the server')

@app.route('/play', defaults={'number': 'x', 'color' : None})
@app.route('/play/<number>', defaults={'color' : None})
@app.route('/play/<number>/<color>')
def play(number, color):
    print("play route visited" + "*"*75)
    # if isinstance(number, int) == False:
    #     print("The input number:" + str(number) +"is not valid" )
    #     number = random.randint(1,25)
    #     numflag = False
    #     print("random number chosen:" + str(number) + "#"*50)
    # else:
    number = int(number) 
    numflag = True

    color = "green"
    # if color == "":
    #     color = "green"
    #     print("random color chosen:" color + "@"*50)
   
    return render_template('play.html', number=number, color=color, numflag=numflag)
  
# @app.route('/play')
# def playtest():
#     print("play route visited" + "*"*75)
#     return render_template('play.html')#, number=3, color='green')
  
                
   
    




if __name__=="__main__":
    app.run(debug=True)