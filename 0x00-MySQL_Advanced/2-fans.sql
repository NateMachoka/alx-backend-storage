-- This script ranks the origin of bands by number of non-unique fans
-- selects the origin of bands and the count of fans
-- ordered by count of fans in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
