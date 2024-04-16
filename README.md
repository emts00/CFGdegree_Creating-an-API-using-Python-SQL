# :cherry_blossom: CFGDegree :purple_heart:
## Assignment 4 Build your own API. 
+ Requirements:
  + Design and implement a simple API as done in class.
  + Remember to come up with a unique creative problem or scenario and show real-life expected use of your database!
+ Marks:
  + A. Design and implementation of an API (33 marks)
  + B. Code readability, layout, and use of best practices (4 marks)
  + C. Creativity (5 marks)
  
**You should:**
+ Implement API endpoints with appropriate functionality
+ Implement one additional endpoint of your choice (can be POST or GET but with a
different implementation)
+ Implement client-side for the 3 API endpoints
+ Create a MySQL database with at least 1 table
+ Have a config file (do not leave your private information here)
+ Have db_utils file and use exception handling
+ Use appropriate SQL queries to interact with the database in your Flask application, and
demonstrate at least two different queries.
+ In main.py have a run() function/call the functions to simulate the planned interaction
with the API, this could include welcome statements, displaying etc., (hairdressers
booking example from lesson)
+ Have correct but minimal imports per file (do not import things you do not use in the
file)
+ Document how to run your API in a markdown file including editing the config file, any
installation requirements up until how to run the code and what is supposed to happen.
+ Submit in GitHub as a Pull Request
+ If time permits:
Optional : Test your API - this is not part of the markscheme, but testing and Test Driven
Development (TDD) are essential skills in programming

**Using GitHub to demonstrate:**
+ Checking the status: [https://github.com/emts00/CFGDegreeAssignment4/blob/main/git-status.PNG](https://github.com/emts00/CFGDegreeAssignment4/blob/main/git-status.PNG)
+ Creating a branch: [https://github.com/emts00/CFGDegreeAssignment4/blob/main/creating-branch.png](https://github.com/emts00/CFGDegreeAssignment4/blob/main/creating-branch.png)
+ Adding files to a branch:  [https://github.com/emts00/CFGDegreeAssignment4/blob/main/git-add-files.png](https://github.com/emts00/CFGDegreeAssignment4/blob/main/git-add-files.png)
+ Adding commits with meaningful messages: [https://github.com/emts00/CFGDegreeAssignment4/blob/main/add-commits-meaningful-msg.png](https://github.com/emts00/CFGDegreeAssignment4/blob/main/add-commits-meaningful-msg.png) 
+ Opening a pull request: [https://github.com/emts00/CFGDegreeAssignment4/blob/main/creating%20a%20pull%20request.png] (https://github.com/emts00/CFGDegreeAssignment4/blob/main/creating%20a%20pull%20request.png)
+ Merging and deploying to the main branch: [https://github.com/emts00/CFGDegreeAssignment4/blob/main/push%20onto%20main%20branch.PNG] 
 (https://github.com/emts00/CFGDegreeAssignment4/blob/main/push%20onto%20main%20branch.PNG)

+ Create .gitignore (can be empty) and briefly explain what it is for. **.gitignore configures git to ignore files you don't want to check into GitHub, it tells git what to ignore when you make a commit.** [https://github.com/emts00/CFGDegreeAssignment4/blob/main/create%20gitignore.PNG](https://github.com/emts00/CFGDegreeAssignment4/blob/main/create%20gitignore.PNG)
  
+ Create requirements.txt (can be empty) and briefly explain what it is for. **It is a file where you can save a list of modules and packages required by your python project.**

  ## Project Management API Documentation: 
:computer: **Overview**
+ Purpose: To keep track of web development projects in a company and have a summary of project details including project name, description, whether it is a high or low priority project, where it is completed, ongoing or to be done, the user assigned, last updated and deadline dates.
+ Functionality: You can add new projects, add new users, assign a user to a project, delete projects, update projects and search for projects already in the database.

**Installation**
+ Requirements
  + Python (version 3.12.2)
  + MySQL (version 8.0.36)

+ Clone the repository: [git clone](https://github.com/emts00/CFGDegreeAssignment4.git)
+ Navigate to the project directory: cd CFGDegreeAssignment4
+ Install dependencies: pip install -r requirements.txt
+ Edit the configuration file config.py to configure database connection settings
  HOST = "127.0.0.1"
  USER = "root"
  PASSWORD = "(Enter yourMySQLpassword here)"

**Running the code**
+ To run a virtual environment:
  + python -m venv env
  + env\Scripts\activate
  
+ Connect the database: run db_utils.py
+ Start the API server: run app.py
+ Run the client side: main.py
+ Use main.py terminal to input what to do


**API Endpoints**
+ GET/getprojects/<project_id>
  + To retrieve project details of a specific project in the database run main.py and input 1 in the command line and choose from the available projects shown in the terminal to see project details.
    + RESPONSE: project name, description, date the project was created on, project priority, project deadline, date that the project was last updated, project status (To do, ongoing, completed), user id assigned to the project


+ GET/get-user/<user_id>
  + To retrieve user details of a specific user in the database run main.py and input 2 in the command line and choose from the available users shown in the terminal to see users' details.
    + RESPONSE: User details: (first name, last name, job title) . User is involved in these projects: (project name, project description)

   
+ GET/get-deadline/<project_id>
  + To retrieve deadline of a specific project in the database run main.py and input 3 in the command line and choose from the available projects shown in the terminal to see project details.
    + RESPONSE: The deadline of project (project_id) is on (YYYY-MM-DD)


+ POST/projectcreation
  + To create a new project, run main.py and input 4 in the command line and input (project name, project description, created date, priority of project (low, medium, high), deadline of project, updated date, project status (To do, ongoing, completed), user id assigned to the project
    + RESPONSE: New project:(project name) has been created.About the project: (project description) Created on: (YYYY-MM-DD). Project prority: (low, medium, high) with the deadline: (YYYY-MM-DD). It was last updated on the (YYYY-MM-DD). Project status is (To do, ongoing, completed). The user ID assigned to this project is (user id)


+ POST/create-user
  + To create a new user, run main.py and input 5 in the command line and input (first name, last name, job title, email
    + RESPONSE: New user:(first name) (last name) has been created. Their role: (job title). Please contact via email (email)

 
+ PUT/update-project_status/<project_status>/<project_id>
  + To update the project status of a specific project, run main.py and input 6 in the command line and input the project id of the project you want to update and the status (to do, ongoing, completed). 
    + RESPONSE: Success! Project (project id) has been updated to (project status)
    + If project id does not exist, it will ask you whether you would like to create a new project, if yes press "Y", if no, press another key and the program will end

 
+ PUT/update-project-user/<user_id>/<project_id>
  + To assign a different user to a specific project, run main.py and input 7 in the command line and input the project id of the project you want to update and the user you would like to assign this project to 
    + RESPONSE: Success! Project (project id) has now been assigned to user ID (user id)
    + If project id does not exist in the database, it will ask you whether you would like to create a new project, if yes press "Y" and it will move to project creation endpoint. If no, press another key and the program will end
    + If user id does not exist, it will ask you whether you would like to create a new user, if yes press "Y", it will move to create-user endpoint. If no, press another key and the program will end

 
+ DELETE/delete-project/<project_id>
  + To delete a project, run main.py and input 8 in the command line and input project id linked to project to delete
    + RESPONSE: Success! Project (project id) has now been deleted or if no such project in database "Project (project id) does not exist!.

+ If you run main.py and input 9 in the command line, it will quit the program
      
