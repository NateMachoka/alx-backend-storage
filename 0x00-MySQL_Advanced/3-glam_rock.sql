-- This script lists all bands with 'Glam Rock' as their main style
-- Ranked by their longevity (until 2022)

SELECT band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
	ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
