-- Createing database, the table and grante select permission
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INT, name VARCHAR(256));
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;
ALTER TABLE nexus6 ADD PRIMARY KEY (id);
ALTER TABLE nexus6 MODIFY id int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;
INSERT INTO nexus6 (name) values ('Leon');

