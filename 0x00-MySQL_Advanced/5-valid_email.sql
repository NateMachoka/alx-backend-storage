-- Thsi script creates a trigger that resets the valid_email attribute
-- when user email is updated

DROP TRIGGER IF EXISTS reset_valid_email_on_email_change;

DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- check if email has changed
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
