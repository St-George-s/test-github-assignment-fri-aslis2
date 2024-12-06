SELECT COUNT(*) AS [Photo Count]
FROM Photos
WHERE photographer_id IN (
    SELECT photographer_id 
    FROM Photographers 
    WHERE experience_years > 5
);