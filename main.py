from db_utils import fetch_projects_ID_table, fetch_user_ID_table, get_project, get_user, get_deadline, delete_project_by_id, update_project_user, create_project, create_new_user, update_project_status
import sys

def get_project_details(project_id):
    result=get_project(project_id)
    return result

def get_user_details(user_id):
    result = get_user(user_id)
    return result

def get_project_deadline(project_id):
    result = get_deadline(project_id)
    return result

def add_project():
    result = create_project()
    return result

def create_user():
    result = create_new_user()
    return result

def update_status(project_status, project_id):
    result= update_project_status(project_status, project_id)
    return result


def update_project(user_id, project_id):
    result= update_project_user(user_id, project_id)
    return result

def delete_project(project_id):
    result = delete_project_by_id(project_id)
    return result


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
