-- script that creates a function SafeDiv that divides (and returns)
-- the first by the second number
-- returns 0 if the second number is equal to 0.

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    -- Check if the second number (b) is 0, if so return 0
    IF b = 0 THEN
        SET result = 0.0;
    ELSE
        SET result = a / b;
    END IF;
    RETURN result;
END //

DELIMITER ;
