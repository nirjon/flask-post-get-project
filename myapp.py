from flask import Flask, request
import json

app = Flask(__name__)

myjokes = ["why did the chicken cross the street? he he"]

@app.route("/getjoke", methods=["GET"])
def get_all_joke():
    x = {"all-jokes" : myjokes}
    return json.dumps(x)

@app.route("/postjoke", methods=["POST"])
def post_new_joke():
    data = request.get_json() #json expected with "joke" key
    myjokes.append(data["joke"])
    return data    

if __name__=='__main__':
    app.run(debug=True)