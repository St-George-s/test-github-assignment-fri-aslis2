SELECT forename, surname, AVG(cost) AS [Average Job Cost]
FROM Customer, Car, Job
WHERE Customer.customerID = Car.customerID AND
 Car.regNo = Job.regNo
GROUP BY cost, forename, surname
ORDER BY AVG(cost) DESC;
