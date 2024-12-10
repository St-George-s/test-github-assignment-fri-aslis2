SELECT forename, surname, SUM(quantity * unitPrice * 1.2) AS [Total to Pay £]
FROM Customer, Gnome, GnomePurchase, Orders
WHERE Orders.orderID="ord0024" 
AND Customer.customerID=Orders.customerID
AND Orders.orderID=GnomePurchase.orderID
AND Gnome.gnomeID=GnomePurchase.gnomeID
GROUP BY Orders.customerID;