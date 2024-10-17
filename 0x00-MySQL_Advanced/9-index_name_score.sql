-- Drop the index if it already exists to avoid errors
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create an index on the first letter of the name and the score
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1), score);
