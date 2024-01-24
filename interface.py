from flask import Flask,jsonify,request
from medical.utils import Medical
app=Flask(__name__)

@app.route("/")

def fun():
    return "Hello"

@app.route("/add")

def add():
    a=100
    b=200
    c=a+b
    return jsonify({"Result":f"the addition of a={a} and b={b} is c={c}"})
@app.route("/input")

def get_input():
    data=request.form
    a=int(data["a"])
    b=int(data["b"])
    c=a+b
    return jsonify({"Result":f"the addition of {a} and {b} is {c}"})

@app.route("/medical")

def get_charges():
    user=request.form
    age=eval(user["age"])
    sex=user["sex"]
    bmi=eval(user["bmi"])
    children=eval(user["children"])
    smoker=user["smoker"]
    region=user["region"]
    med_ins=Medical(age,sex,bmi,children,smoker,region)
    result=med_ins.get_predicted_charges()

    return jsonify({"Result":f"the predicted charges is {result}"})

if __name__=="__main__":
    app.run()
