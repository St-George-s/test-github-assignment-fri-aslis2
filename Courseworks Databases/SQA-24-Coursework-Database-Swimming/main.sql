SELECT initial, surname, swimCategory, teamName, COUNT(raceNumber) AS [Races won] 
FROM Swimmer, Result, Team 
WHERE Swimmer.swimmerID = Result.swimmerID and Swimmer.teamRef = Team.teamRef and position = 1 
GROUP BY surname 
ORDER BY initial ASC; 


SELECT initial, surname, teamName, city, eventDate 
FROM Swimmer, Result, Team, Event, Race, (SELECT MIN(raceTime) as fastestTime 
FROM Result WHERE (lane = 1) or (lane = 8)) 
WHERE Team.teamRef = Swimmer.teamRef and Swimmer.swimmerID = Result.swimmerID and Result.raceNumber = Race.raceNumber and Race.eventID = Event.eventID and raceTime = fastestTime and (lane = 1 or 8) 
GROUP by Swimmer.swimmerID; 


SELECT teamName, COUNT(position) AS [Total medals won]
FROM Result, Swimmer, Team
WHERE Result.swimmerID = Swimmer.swimmerID AND Swimmer.teamRef = 
Team.teamRef and (position = 1 or position= 2 or position =3)
GROUP BY teamName
ORDER BY COUNT(position) DESC;

