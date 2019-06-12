CREATE DATABASE IF NOT EXISTS sling;
USE sling;
CREATE USER IF NOT EXISTS 'sling'@'localhost';
SET PASSWORD FOR 'sling'@'localhost' = 's';
GRANT ALL PRIVILEGES ON sling.* TO 'sling'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
