from flask import Flask, request, render_template, redirect, url_for
import random
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that the 404 status is set explicitly. I.e. this errorhandler only handles 404 errors
    return "Sorry! No response. Try again"

@app.route('/')
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users=users)





if __name__=="__main__":
    app.run(debug=True)