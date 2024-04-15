#pip install flask
#pip install flask-mysqldb
# pip install mysql.connector
# pip install --upgrade mysql-connector-python 
from datetime import datetime as dt
import mysql.connector
import sys
from config import USER, PASSWORD, HOST

def _connect_to_db():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
    )
    print("Connected to DB: %s" % mydb)

    return mydb

_connect_to_db()

def get_all_database():
    db_connection = _connect_to_db()
    mycursor = db_connection.cursor()
    mycursor.execute('SHOW DATABASES')
    for x in mycursor:
        print(x)

# get_all_database()

def _connect_to_specific_db(project_management):
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database = project_management
    )
    print("Connected to DB: %s" % mydb)

    return mydb

db_name = "project_management"
_connect_to_specific_db(db_name)

def _show_all_table_in_specific_db(db_name):
      specific_db = _connect_to_specific_db(db_name)
      mycursor = specific_db.cursor()
      mycursor.execute("SHOW TABLES")
      
      for x in mycursor:
            print(x)

      mycursor.close()

db_name = "project_management"
_show_all_table_in_specific_db(db_name)

class DbConnectionError(Exception):
    pass
class ProjectNotFoundError(Exception):
    pass

def fetch_projects_ID_table():
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = "SELECT * FROM projects"
  
        mycursor.execute(query)
        result = mycursor.fetchall()

        print("Project id available:")
        for row in result:
            project_id = row[0],
            project_name = row[1]
            print("project_id:", project_id)
            print("project_name:", project_name)

        mycursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB.") 
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def fetch_user_ID_table():
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = "SELECT * FROM user_data"
  
        mycursor.execute(query)
        result = mycursor.fetchall()

        print("User id's available:")
        for row in result:
            user_id = row[0],
            print("user_id:", user_id)
            
        mycursor.close() 


    except Exception:
        raise DbConnectionError("Failed to read data from DB.") 
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# Search for a specific project and get ALL project details for it 
def get_project(project_id):
    projects_dict = {}
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        if project_id is None:
            result = []
            raise Exception("Project ID not found in database")
       
        query = "SELECT project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id FROM projects WHERE project_id = {};".format(project_id) 
        mycursor.execute(query)
        result = mycursor.fetchone()

        if result is None:
            print("Project {} does not exist".format(project_id))
        else:
            query = "SELECT project_id, project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id FROM projects WHERE project_id = {};".format(project_id) 
            mycursor.execute(query)
            result2 = mycursor.fetchall()
            for row in result2:
                project_id, project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id = row
                projects_dict[project_id] = {
                    "project_name": project_name,
                    "project_description": project_description,
                    "created_on": created_on,
                    "priority": priority,
                    "deadline": deadline,
                    "updated_on": updated_on,
                    "project_status": project_status,
                    "user_id": user_id
    }
                print("Project details:")
                for project_id, project_data in projects_dict.items():
                    print(f"Project ID: {project_id}, Project Data: {project_data}")
        mycursor.close() 
             

    except Exception:
        raise DbConnectionError("Failed to read data from DB.") 
    
    
    finally:
        
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# get_project(1)  

# #Retrieve deadline of a project
def get_deadline(project_id):
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        if project_id is None:
            raise Exception("Project ID not found in database")
        
        query = "SELECT p.deadline, u.job_title, u.first_name, u.last_name FROM user_data u JOIN projects p ON u.user_id = p.user_id WHERE p.project_id = {};".format(project_id) 
        mycursor.execute(query)
        result = mycursor.fetchall()

        if result is None:
            print("Project {} does not exist".format(project_id))
        else:
            for i in result:
                print("The deadline of project {} is on (YYYY-MM-DD) {} is assigned to this project ".format(project_id, i))
        mycursor.close()      

    except Exception:
        raise DbConnectionError("Failed to read data from DB") 
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
# get_deadline(2)

# #Retrieve user details then which project they are involved in if any and when they last updated the project.
def get_user(user_id):
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        if user_id is None:
            raise Exception("User ID not found in database")
        query1 = "SELECT first_name, last_name, job_title FROM user_data WHERE user_id = {}".format(user_id)
        mycursor.execute(query1)
        print("User {}'s details: ".format(user_id))
        result = mycursor.fetchone()
        
        if result is None:
            print("User {} does not exist".format(user_id))
            raise Exception("User ID not found in database")
        else:
            for i in result:
                print(i)
        query2 = "SELECT p.project_name, p.project_description FROM user_data u JOIN projects p ON u.user_id = p.user_id WHERE u.user_id = {}".format(user_id) 
        mycursor.execute(query2)
        print("User {} was involved in these projects: ".format(user_id))
        result2 = mycursor.fetchone()
        if result2 is None:
            print("User {} is not involved in any projects".format(user_id))
        else:
            for i in result2:
                print(i)
            mycursor.close()          

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
# get_user(1)


# #Create a new project
# @app.route("/create-project", methods=["POST"])
def create_project():
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        print("Connected to DB: %s" % db_name)

        project_name = input("Enter Project Name: ")
        project_description = input("Enter Project Description: ")
        created_date = dt.strptime(input("Enter the date that the project was created on in the YYYY-MM-DD format: "),'%Y-%m-%d')
        created_on = created_date.strftime('%Y-%m-%d')
        priority = input("Enter priority for project priority (HIGH, MEDIUM, LOW): ").upper()
        while priority not in ["HIGH", "MEDIUM","LOW" ]:
            priority = input("Enter priority for project priority (HIGH, MEDIUM, LOW): ").upper()
        else:
            print("Project priority is {}".format(priority))
        deadline_date = dt.strptime(input("Enter the date of project deadline in the YYYY-MM-DD format): "), '%Y-%m-%d')
        if deadline_date > created_date:
            deadline = deadline_date.strftime('%Y-%m-%d')
        else:
            print("Project deadline date must be after created on date")
            print("goodbye")
            sys.exit()

        updated_date = dt.strptime(input("Enter date of when project was last updated in the YYYY-MM-DD format: "), '%Y-%m-%d')
        if updated_date == created_date or updated_date > created_date:
            updated_on = updated_date.strftime('%Y-%m-%d')
        else:
            print("Date that project was updated must be on or after created on date")
            print("goodbye")
            sys.exit()
        project_status= input("Enter project status (TO DO, ONGOING, COMPLETED): ").upper()
        while project_status not in ["TO DO", "ONGOING", "COMPLETED"]:
            project_status= input("INVALID INPUT. Enter project status (TO DO, ONGOING, COMPLETED):  ").upper()
        else:
            print("Project status is {}".format(project_status))
        user_id = int(input("Type the User ID assigned to this project: "))

        mycursor = db_connection.cursor()
        query = "INSERT INTO projects (project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id)
        
        mycursor.execute(query,values)
        db_connection.commit()
        print("New project:{} has been created.\nAbout the project: {}. \nCreated on: {}. \nProject prority: {} with the deadline: {}. \nIt was last updated on the {}. \nProject status is {}. \nThe user ID assigned to this project is {}.".format(project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id))
        mycursor.close() 
        
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# #Create a new user
def create_new_user():
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        print("Connected to DB: %s" % db_name)

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        job_title = input("Enter Job title: ")
        email = input("Enter Email: ")

        mycursor = db_connection.cursor()
        query = "INSERT INTO user_data (first_name, last_name, job_title, email) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, job_title, email)
        
        mycursor.execute(query,values)
        db_connection.commit()
        print("New user:{} {} has been created. Their role: {}. Please contact via email {}".format(first_name, last_name, job_title, email))
        mycursor.close() 

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# #Update the status of a project
def update_project_status(project_status, project_id):
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query1 = "SELECT project_id FROM projects WHERE project_id = {}".format(project_id)  
        mycursor.execute(query1)
        result=mycursor.fetchone()

        if result is None:
            print("Project {} does not exist".format(project_id))
            project_yes= input("Would you like to create a new project? (y/n):").upper()
            
            if project_yes == "Y":
                create_project()
            else: 
                print("goodbye")
                sys.exit()

        else:
            query2 = "UPDATE projects SET project_status = {} WHERE project_id = {}".format(project_status, project_id)  
            mycursor.execute(query2)
            db_connection.commit() 
            print("Success! Project {} has been updated to {}.".format(project_id, project_status))
        mycursor.close()     

    except Exception:
        raise ProjectNotFoundError("Project ID not found in database")
    
    
    finally:
         
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# #Assign a different user to a project
def update_project_user(user_id, project_id):
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query1 = "SELECT * FROM projects WHERE project_id = {}".format(project_id)  
        mycursor.execute(query1)
        result1=mycursor.fetchone()

        query2 = "SELECT * FROM user_data WHERE user_id = {}".format(user_id)  
        mycursor.execute(query2)
        result2=mycursor.fetchone()

        if result1 is None:
            print("Project {} does not exist".format(project_id))
            project_yes= input("Would you like to create a new project? (y/n):").upper()
            
            if project_yes == "Y":
                create_project()
            else: 
                print("goodbye")
                sys.exit()

        elif result2 is None:
            print("User {} does not exist".format(user_id))
            newuser_yes= input("Would you like to create a new user? (y/n):").upper()
            
            if newuser_yes == "Y":
                create_new_user()
            else:
                print("goodbye")
                sys.exit()

        else:
            query3 = "UPDATE projects SET user_id = {} WHERE project_id = {}".format(user_id, project_id) 
            mycursor.execute(query3)
            db_connection.commit()
            print("Success! Project {} has now been assigned to user ID {}".format(project_id, user_id))
        mycursor.close()      

    except Exception:
        raise ProjectNotFoundError("Project ID not found in database")
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")   

def delete_project_by_id(project_id):
    try:
        db_name = "project_management"
        db_connection =  _connect_to_specific_db(db_name)
        mycursor = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query1 = "SELECT project_id FROM projects WHERE project_id = {}".format(project_id)  
        mycursor.execute(query1)
        result=mycursor.fetchone()

        if result is None:
            print("Project {} does not exist".format(project_id))
            print("goodbye")
            sys.exit()
        else:
            query2 = "DELETE FROM projects WHERE project_id = {};".format(project_id) 
            mycursor.execute(query2)
            db_connection.commit()
            print("Success! Project {} has now been deleted.".format(project_id))   

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")






# if __name__ == '__main__':
    # print(get_all_booking_availability('2024-04-15'))
    # add_booking("2024-04-15", "Magdalena", "12-13", "Sam")
    # print(get_all_booking_availability('2024-04-15'))
    #is this where i print out the database in terminal after get, put, post and delete requests?