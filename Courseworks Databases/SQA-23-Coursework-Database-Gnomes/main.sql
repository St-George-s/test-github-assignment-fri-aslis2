
SELECT gnomeName, SUM(quantity) as [Total gnomes sold]
FROM Gnome, GnomePurchase
WHERE Gnome.gnomeID = GnomePurchase.gnomeID and description like "%solar%"
GROUP BY gnomeName
ORDER BY SUM(quantity) DESC;


SELECT emailAddress, Orders.orderID, quantity 
FROM Customer, Orders, GnomePurchase, Gnome 
WHERE Customer.customerID=Orders.customerID  
    AND Orders.orderID=GnomePurchase.orderID 
    AND GnomePurchase.gnomeID=Gnome.gnomeID 
    AND quantity >= 3 
    AND unitPrice = ( SELECT MAX(unitPrice) FROM Gnome ); 


SELECT forename, surname, SUM(quantity * unitPrice * 1.2) AS [Total to Pay £]
FROM Customer, Gnome, GnomePurchase, Orders
WHERE Orders.orderID="ord0024" 
AND Customer.customerID=Orders.customerID
AND Orders.orderID=GnomePurchase.orderID
AND Gnome.gnomeID=GnomePurchase.gnomeID
GROUP BY Orders.customerID;