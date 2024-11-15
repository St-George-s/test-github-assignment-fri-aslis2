SELECT title, date_taken 
FROM Photos 
WHERE date_taken = (SELECT MAX(date_taken) FROM Photos);