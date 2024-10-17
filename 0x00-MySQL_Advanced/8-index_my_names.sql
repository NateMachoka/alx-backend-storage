-- Drop the index if it already exists to avoid errors
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create an index on the first letter of the name
CREATE INDEX idx_name_first ON names (name(1));
