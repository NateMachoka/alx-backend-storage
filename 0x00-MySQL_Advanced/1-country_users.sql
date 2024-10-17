-- This table creates a table 'users' with the following attributes
-- id: integer, never null, auto-increment, primary key
-- email: string(255) never null and unique
-- name: string(255)
-- country: ENUM ('US', 'CO', 'TN') never nulll, default 'US'
-- If table exits, script won't fail

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id),
    UNIQUE (email)
    );
