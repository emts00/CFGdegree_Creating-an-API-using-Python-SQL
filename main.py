
import requests
from db_utils import fetch_projects_ID_table, fetch_user_ID_table, get_project, get_user, get_deadline, delete_project_by_id, update_project_user, create_project, create_new_user, update_project_status
import sys

def get_project_details(project_id):
    result = requests.get('http://127.0.0.1:5000/getprojects/{}'.format(project_id),
                          headers= {'content-type': 'application/json'}
    )
    get_project(project_id)
    return result.json()

def get_user_details(user_id):
    result = requests.get('http://127.0.0.1:5000/get-user/{}'.format(user_id),
                          headers= {'content-type': 'application/json'}
    )
    get_user()
    return result.json()

def get_project_deadline(project_id):
    result = requests.get('http://127.0.0.1:5000/deadline/{}'.format(project_id),
                          headers= {'content-type': 'application/json'}
    )
    get_deadline()
    return result.json()

def add_project():
    result = requests.post('http://127.0.0.1:5000/projectcreation',
                          headers= {'content-type': 'application/json'}
    )
    create_project()
    return result.json()

def create_user():
    result = requests.post('http://127.0.0.1:5000/create-user',
                          headers= {'content-type': 'application/json'},
    )
    create_new_user()
    return result.json()

def update_status(project_status, project_id):
    result= requests.put('http://127.0.0.1:5000/update-project_status/{}/{}'.format(project_status, project_id),
                          headers= {'content-type': 'application/json'}
    )
    update_project_status()
    return result.json()


def update_project(user_id, project_id):
    result= requests.put('http://127.0.0.1:5000/update-project-user/{}/{}'.format(user_id, project_id),
                          headers= {'content-type': 'application/json'},
                          
    )
    update_project_user()
    return result.json()

def delete_project(project_id):
    result = requests.delete('http://127.0.0.1:5000/delete-project/{}'.format(project_id),
                          headers= {'content-type': 'application/json'}
    )
    delete_project_by_id()
    return result.json()


def run():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to Project Management')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print('\n 1= Search for a project, \n 2= Search for a user, \n 3= View project deadline and user assigned, \n 4= Add a new project, \n 5= Add a new user, \n 6= Update a project status, \n 7= Assign a different user to a project, \n 8= Delete a project, \n 9= QUIT') 
    user_input = int(input('What would you like to do? (Please enter a number) '))
    print('You selected {}'.format(user_input))
    
    if user_input == 1:
        fetch_projects_ID_table()
        project_id = int(input("Type the project id: "))
        get_project(project_id)

        
    elif user_input == 2:
        fetch_user_ID_table()
        user_id = int(input("Type the user id: "))
        get_user(user_id)


    elif user_input == 3:
        fetch_projects_ID_table()
        project_id = int(input("Type the project id: "))
        get_deadline(project_id)


    elif user_input == 4:
        create_project()


    elif user_input == 5:
        create_new_user()


    elif user_input == 6:
        fetch_projects_ID_table()
        project_id = int(input("Type the project id: "))
        status = input("Type the project status (TO DO, ONGOING, COMPLETED): ").upper()
        if status not in ["TO DO", "ONGOING", "COMPLETED"]:
            status= input("INVALID INPUT. Enter project status (TO DO, ONGOING, COMPLETED):  ").upper()
        else:
            project_status= f'"{status}"'
            print("Project {} status is {}".format(project_id, project_status))
        update_project_status(project_status, project_id)
        

    elif user_input == 7:
        fetch_projects_ID_table()
        project_id = int(input("Type the project id: "))
        fetch_user_ID_table()
        user_id = int(input("Type the user id: "))
        update_project_user(user_id, project_id)

    elif user_input == 8:
        fetch_projects_ID_table()
        project_id = int(input("Type the project id: "))
        delete_project_by_id(project_id)

    elif user_input == 9:
        print("goodbye")
        sys.exit()

    else:
        print("goodbye")
        sys.exit()

if __name__ == '__main__':
    run()