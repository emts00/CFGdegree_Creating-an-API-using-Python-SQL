from flask import Flask, jsonify
from main import get_project_details, get_user_details, get_project_deadline, update_project, update_status, delete_project, add_project, create_user
  
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Project Management!"

@app.route('/getprojects/<project_id>')
def get_a_project(project_id):
    return get_project_details(project_id)

@app.route('/get-user/<user_id>')
def get_a_user(user_id):
    try:
        get_user_details(user_id)
        return jsonify({"message": "Success: Retrieved Project details"}), 200
    except Exception:
        return jsonify({"message": "Failed to retrieve user"}), 500 

@app.route('/get-deadline/<project_id>')
def get_project_deadline_route(project_id):
    try:
        get_project_deadline(project_id)
        return jsonify({"message": "Success: Retrieved Project deadline"}), 200
    except Exception:
        return jsonify({"message": "Failed to retrieve project deadline"}), 500 

@app.route("/projectcreation", methods=["POST"])
def add_project_route():
    try:
        add_project()
        return jsonify({"message": "Success: Project created"}), 200
    except Exception:
        return jsonify({"message": "Failed to create project"}), 500 


@app.route("/create-user", methods=["POST"])
def create_user_route():
    try:
        create_user()
        return jsonify({"message": "User created successfully"}), 200
    except Exception:
        return jsonify({"message": "Failed to create user"}), 500 

@app.route("/update-project_status/<project_status>/<project_id>", methods=["PUT"])
def update_project_status_route(project_status,project_id):
    try: 
        update_status(project_status, project_id)
        return jsonify({"message": "Success: Project status updated"}), 200
    except Exception:
        return jsonify({"message": "Failed to update project status"}), 500 


@app.route("/update-project-user/<user_id>/<project_id>", methods=["PUT"])
def update_project_route(user_id, project_id):
    try: 
        update_project(user_id, project_id)
        return jsonify({"message": "Success: Project user updated"}), 200
    except Exception:
        return jsonify({"message": "Failed to update project user"}), 500 


@app.route('/delete-project/<project_id>', methods=['DELETE']) 
def delete_project_route(project_id):
    try: 
        delete_project(project_id)
        return jsonify({"message": "Success: Project deleted"}), 200
    except Exception:
        return jsonify({"message": "Failed to delete project"}), 500 


if __name__ == '__main__':
    app.run(debug=True)  #will run our flask server


    