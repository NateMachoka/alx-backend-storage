-- This script creates a table 'users' with an id, email, and name
-- The id is an auto-incremented primary key
-- email is unique and not null
-- checks if the table already exists before creating it

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);
