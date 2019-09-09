from flask import Flask, request, render_template, redirect, url_for
import random
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that the 404 status is set explicitly. I.e. this errorhandler only handles 404 errors
    return "Sorry! No response. Try again"


    # our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form,"#"*25)
    name = request.form['name']
    email = request.form['email']
    platform = request.form['platform']
    commutes = request.form.getlist('commute')
    print(commutes,"*"*50)

    



    # email_from_form = request.form['email']
    return render_template("show.html", name=name, email=email, platform=platform, commutes=commutes)

#commutes=commute



if __name__=="__main__":
    app.run(debug=True)