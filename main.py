#pip3 install flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app .route("/") #make this accessible
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "first_name": "John",
        "last_name": "Doe",
        "job_title": "manager",
        "email": "johndoe@example.com"
    }

    extra = request.args.get("extra") # "get-user/123?extra=hello world"  #Addtional variable that can be passed along to the root
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200 # return data from API, we will use JSON, 200 default for success HTTP status code

@app.route("/create-user", methods=["POST"])
def create_user():
    data=request.get_json()

    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True) #will run our flask server


