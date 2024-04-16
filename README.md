# :cherry_blossom: CFGDegree :purple_heart:
## Assignment 4 Build your own API. Requirements:
Design and implement a simple API as done in class.
Remember to come up with a unique creative problem or scenario and show real-life expected
use of your database!
Marks:
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
+ Checking the status: [https://github.com/emts00/CFGDegreeSpring2024/master/git-status.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/git-status.png)
+ Creating a branch:[ https://github.com/emts00/CFGDegreeSpring2024/master/creating-branch.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/creating-branch.png)
+ Adding files to a branch:  [ https://github.com/emts00/CFGDegreeSpring2024/master/git-add-files.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/git-add-files.png)
+ Adding commits with meaningful messages:[ https://github.com/emts00/CFGDegreeSpring2024/master/add-commits-meaningful-msg.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/add-commits-meaningful-msg.png)
+ Opening a pull request: [https://github.com/emts00/CFGDegreeSpring2024/master/opening-pull-request.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/opening-pull-request.png)
+ Merging and deploying to the main branch: [ https://github.com/emts00/CFGDegreeSpring2024/master/push-to-main-branch.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/push-to-main-branch.png)

+ Create .gitignore (can be empty) and briefly explain what it is for. **.gitignore configures git to ignore files you don't want to check into GitHub, it tells git what to ignore when you make a commit.** [https://github.com/emts00/CFGDegreeSpring2024/master/created-.gitignore.png](https://github.com/emts00/CFGDegreeSpring2024/blob/master/created-.gitignore.png)
  
+ Create requirements.txt (can be empty) and briefly explain what it is for. **It is a file where you can save a list of modules and packages required by your python project.**

  ## Project Management API Documentation: 
:computer: **Overview**
+ Purpose: To keep track of web development projects in a company and have a summary of project details including project name, description, whether it is a high or low priority project, where it is completed, ongoing or to be done, the user assigned, last updated and deadline dates.
+ Functionality: You can add new projects, add new users, assign a user to a project, delete projects, update projects and search for projects already in the database.

**Installation**
Requirements
+ Python (version 3.12.2)
+ MySQL (version 8.0.36)

+ Clone the repository: [git clone](https://github.com/emts00/CFGDegreeSpring2024.git)
+ Navigate to the project directory: cd CFGDegreeSpring2024
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
