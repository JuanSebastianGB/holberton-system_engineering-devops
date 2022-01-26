-- Creating a new user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'userpwd';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
