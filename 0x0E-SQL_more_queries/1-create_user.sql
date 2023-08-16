-- script that creates the MySQL server user user_0d_1.
-- cript that creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT 
ON *.* 
TO 'user_0d_1'@'localhost';
