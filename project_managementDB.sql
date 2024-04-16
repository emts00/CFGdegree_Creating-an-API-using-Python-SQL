-- CREATE DATABASE project_management;

USE project_management;

-- CREATE TABLE user_data (
-- 	user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     job_title VARCHAR(100),
--     email VARCHAR(100)
-- );

-- CREATE TABLE projects (
-- 	project_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
--     project_name VARCHAR(100) NOT NULL, 
--     project_description TEXT,
--     created_on DATETIME,
--     priority ENUM('LOW', 'MEDIUM', 'HIGH'),
--     deadline DATETIME NOT NULL,
-- 	updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     project_status ENUM('TO DO', 'ONGOING', 'COMPLETED'),
--     user_id INT,
--     FOREIGN KEY user_assigned (user_id)
--     REFERENCES user_data (user_id)
-- );
-- INSERT INTO user_data (user_id, first_name, last_name, job_title, email) VALUES
-- (1, "John" , "Smith", "E-Learning Instructor", "JSmith@gmail.com"),
-- (2, "Jo", "Ellis", "Junior Developer", "JEllis@gmail.com"),
-- (3, "Elle", "Turner", "Full Stack Developer", "ETurner@hotmail.com"),
-- (4, "Bob", "Johnson", "Manager", "BobJohnson@gmail.com");

-- INSERT INTO projects (project_id, project_name, project_description, created_on, priority, deadline, updated_on, project_status, user_id) VALUES
-- ( 1, "Online Learning Platform", "Develop an online learning platform where users can access courses, participate in quizzes and track gaps in knowledge",'2024-04-11', 'LOW', '2024-06-22', '2024-04-12','TO DO', 1),
-- ( 2, "Fitness Tracking Platform", "Develop a fitness tracking app where users can set fitness goals, track their workouts, and monitor their progress.", '2024-03-20', 'HIGH', '2024-05-15', '2024-04-13','ONGOING', 2);
