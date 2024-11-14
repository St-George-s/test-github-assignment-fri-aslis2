--  SELECT  A.album_name, T.track_name
--  FROM Tracks T, Albums A
--  WHERE A.release_year > 2020;


SELECT * FROM Albums
ORDER BY release_year ASC;

 SELECT T.track_name, A.album_name 
 FROM Tracks T, Albums A
 WHERE T.album_id = A.album_id
   AND A.release_year > 2020
GROUP BY T.track_name;

 SELECT T.track_name, T.track_id, A.album_id
 FROM Tracks T, Albums A
  WHERE T.album_id = A.album_id
and A.album_id IN (3,25,31,57);