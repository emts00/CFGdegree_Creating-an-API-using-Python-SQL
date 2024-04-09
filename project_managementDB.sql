CREATE DATABASE project_management;

USE project_management;

CREATE TABLE projects (
	project_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL, 
    project_description TEXT,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    priority ENUM('LOW', 'MEDIUM', 'HIGH')
);
CREATE TABLE deadline (
	project_id INT,
	FOREIGN KEY (project_id)
	REFERENCES projects (project_id),
    deadline DATE NOT NULL PRIMARY KEY,
	updated_on DATETIME,
    project_status ENUM('TO DO', 'ONGOING', 'COMPLETED')
);

CREATE TABLE user_data (
	user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE project_tasks (
	project_id INT,
	FOREIGN KEY (project_id)
	REFERENCES projects (project_id),
    task_id DECIMAL(2,1) NOT NULL PRIMARY KEY,
    task VARCHAR(255),
    task_status ENUM('TO DO', 'ONGOING', 'COMPLETED')
);

CREATE TABLE tasks_assigned (
    user_id_assigned INT,
    FOREIGN KEY (user_id)
	REFERENCES users (user_id),
    project_id INT,
	FOREIGN KEY (project_id)
	REFERENCES projects (project_id),
    task_id DECIMAL (2,1),
	FOREIGN KEY (task_id)
	REFERENCES project_tasks (task_id)
);

CREATE TABLE user_task_reflection (
	user_id_assigned INT,
    FOREIGN KEY (user_id)
	REFERENCES users (user_id),
    project_id INT,
	FOREIGN KEY (project_id)
	REFERENCES projects (project_id),
    task_id DECIMAL (2,1),
	FOREIGN KEY (task_id)
	REFERENCES project_tasks (task_id),
    achievement_reflection TEXT
);




