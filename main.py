from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
caesar_form ="""

<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            
        </style>
    </head>
    <body>
    <!-- create your form here -->
     <form method ='POST'> 
        <label for = "rot_k">Rotate by:</label>
        <input name = "rot" id = "rot_k" type = "text" value = 0 />
        <br>

        <textarea name = "text">{final_text}</textarea>
        
        <input type = "submit" value = "submit"/>
     </form>
    </body>
  </html>
"""
@app.route("/", methods = ['POST'])
def encrypt():
        
   rotnum = int(request.form['rot'])
   textmess = request.form['text']
   new_text = rotate_string(textmess,rotnum)
   return caesar_form.format(final_text = new_text)



@app.route("/")
def index():
    return caesar_form.format(final_text = '')

app.run()