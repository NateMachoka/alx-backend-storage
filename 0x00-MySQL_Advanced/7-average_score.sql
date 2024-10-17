-- This script that creates a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate average score from corrections table
    SELECT AVG(c.score) INTO avg_score
    FROM corrections AS c
    WHERE c.user_id = user_id;

    -- Update the user's average_score in the users table
    UPDATE users AS u
    SET u.average_score = avg_score
    WHERE u.id = user_id;
END //

DELIMITER ;
