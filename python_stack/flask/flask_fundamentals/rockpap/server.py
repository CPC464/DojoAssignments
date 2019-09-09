from flask import Flask, request, render_template, redirect, url_for, session
import random
app = Flask(__name__)

session['win']=0
session['loos']=0
session['draw']=0


def rps(user_choice):
    choices = ["scissors", "paper", "rock"]
    cp_choice = random.choice(choices)
    results = {
        "rock" : {"rock" : "tie", "paper" : "lose" , "scissors" : "win"},
        "paper" : {"rock" : "win", "paper" : "tie" , "scissors" : "lose"},
        "scissors" : {"rock" : "lose", "paper" : "win" , "scissors" : "tie"},
    }
    return results[user_choice][cp_choice]   

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/choice", methods=['POST'])
def choice():
    print("Choice route reached" + "#"*50)
    user_choice = request.form['user_choice']
    print(user_choice + "*"*50)
    result = rps(user_choice) 

    session['user_choice'] = user_choice
    session['cp_choice'] = cp_choice
    session['latest_result'] = result
    session[result] += 1 
    return redirect("/")




if __name__=="__main__":
    app.run(debug=True)