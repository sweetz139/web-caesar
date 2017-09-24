from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
caesar_form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <!-- create your form here -->
    <form action = "/hello" methods = ['POST']> 
    <label>Rotate by:<input type = "text" name = "rot"></label>
    <br></br>
    <input type = "textarea" name = "text">
    <input type = "submit">
    </form>
    </body>
<html>
"""
@app.route("/",methods = ['POST'])
def encrypt():

    return "hello"

@app.route("/")
def index():

    
    return caesar_form

app.run()