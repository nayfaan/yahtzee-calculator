import services.yahtzee
from services.yahtzee import *
import services.startDriver
from services.startDriver import *

from celery import Celery

#Flask: Web app wrapper
from flask import Flask, render_template, request, escape, url_for, redirect, make_response
from flask import jsonify
from flask_restful import Resource, Api


app = Flask(__name__,
            static_url_path="",
            static_folder="web/static",
            template_folder="web/templates")
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

#Starting web app
@app.route("/index", methods=["GET", "POST", "PUT"])
def index():
    global dice_1, dice_2, dice_3, dice_4, dice_5
    global yahtzee
    
    #idfk where this came from
    if request.method == "GET":
        return render_template("index.html", dice_1=dice_1, dice_2=dice_2, dice_3=dice_3, dice_4=dice_4, dice_5=dice_5)
    
    #background process: clicking
    elif request.method == "PUT":
        return jsonify({})
        
    
    #post method, only called at initiation (?)
    else:
        yahtzee = yahtzee
        
        return render_template("index.html", dice_1=dice_1, dice_2=dice_2, dice_3=dice_3, dice_4=dice_4, dice_5=dice_5)

@celery.task
def start_flask():
    app.run(host="127.0.0.1", port=8080, debug=True)
    
def start_driver():
    try:        
        driver = services.startDriver.start()
        try:
            driver.get("http://127.0.0.1:8080/")
        except:
            pass
    except:
        pass

def main():
    task = start_flask.delay()
    start_driver()
    

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    main()
