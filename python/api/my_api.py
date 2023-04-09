from crypt import methods
from unicodedata import name
from flask import *
import json, datetime


k= datetime.datetime.now()
l=k.strftime("%Y-%m-%d %H:%M:%S")

app= Flask(__name__)



@app.route("/", methods=['GET'])
def landing_page():
    data_set= {
        "Page": "Home",
        "message":"Success 202!",
        "Time": l
    }
    json_dumps = json.dumps(data_set)

    return json_dumps


@app.route("/user/", methods=['GET'])
def user_page():
    usr= str(request.args.get("user"))
    data_set= {
        "Page": "user page",
        "message":f"Success 200! Welcome {usr}!! ",
        "Time": l
    }
    json_dumps = json.dumps(data_set)

    return json_dumps
   
if __name__=='__main__':
    app.run(debug=True,port=7778)

