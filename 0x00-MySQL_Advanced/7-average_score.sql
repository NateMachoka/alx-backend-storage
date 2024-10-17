-- This script that creates a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_scores FLOAT;

	SELECT AVG(c.score) INTO avg_scores FROM corrections AS c
	WHERE user_id = c.user_id;

	UPDATE users AS u
	SET u.average_score = avg_scores
	WHERE u.id = user_id;
END//

DELIMITER ;
