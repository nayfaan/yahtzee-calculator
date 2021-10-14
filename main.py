import services.yahtzee
from services.yahtzee import *

#Flask: Web app wrapper
from flask import Flask, render_template, request, escape, url_for, redirect, make_response
from flask import jsonify

app = Flask(__name__,
            static_url_path="",
            static_folder="web/static",
            template_folder="web/templates")

#Starting web app
@app.route("/", methods=["GET", "POST", "PUT"])
def index():
    global dice_1, dice_2, dice_3, dice_4, dice_5
    global yahtzee
    
    #idfk where this came from
    if request.method == "GET":
        return render_template("index.html")#, dice_1=dice_1, dice_2=dice_2, dice_3=dice_3, dice_4=dice_4, dice_5=dice_5)
    
    #background process: clicking
    elif request.method == "PUT":
        return jsonify({})
        
    
    #post method, only called at initiation (?)
    else:
        yahtzee = yahtzee
        
        return render_template("index.html", dice_1=dice_1, dice_2=dice_2, dice_3=dice_3, dice_4=dice_4, dice_5=dice_5)
    
    
def main():
    app.run(host="localhost", port=8080, debug=True)
    

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    main()
