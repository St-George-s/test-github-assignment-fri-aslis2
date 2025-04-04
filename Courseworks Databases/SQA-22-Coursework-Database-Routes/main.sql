SELECT Planner.forename, Planner.surname, Planner.plannerNo, COUNT(walkerNo) AS [Total Participants] 
FROM Planner, Route, Walk 
WHERE Planner.plannerNo=Route.plannerNo  
AND Route.routeID=Walk.routeID  
GROUP BY Planner.plannerNo 
ORDER BY COUNT(walkerNo) DESC; 


SELECT Walker.walkerNo, forename, surname, telNo 
FROM Walker, Walk, Route 
WHERE Walker.walkerNo=Walk.walkerNo  
AND Walk.routeID=Route.routeID  
AND distance =(SELECT MAX(distance) FROM Route) 
GROUP BY Walker.walkerNo 
ORDER BY Walker.walkerNo ASC; 


SELECT Route.routeID, woodName, description
FROM Route
WHERE footwear LIKE "%shoe%";