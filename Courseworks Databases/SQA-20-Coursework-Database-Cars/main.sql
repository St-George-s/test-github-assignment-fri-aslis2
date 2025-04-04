SELECT garageName, SUM(cost) as [Total sales]
FROM Garage, Job
WHERE Garage.garageID == Job.garageID
GROUP BY Garage.garageID;

SELECT [Number of Days], 
Job.regNo, garageName
FROM (SELECT Max(dateOut-dateIn) 
AS [Number of Days]
FROM Job), Job, Garage
WHERE (dateOut-dateIn) = 
[Number of Days] AND 
Job.garageID = 
Garage.garageID;

SELECT forename, surname, AVG(cost) AS [Average Job Cost]
FROM Customer, Car, Job
WHERE Customer.customerID = Car.customerID AND
 Car.regNo = Job.regNo
GROUP BY forename, surname, Customer.customerID
ORDER BY AVG(cost) DESC;
