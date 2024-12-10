SELECT name, COUNT(bookingID) as [Total Bookings]
FROM Shop, Event, Booking 
Where Shop.shopID == Event.shopID and Event.eventID == Booking.eventID
Group by Shop.shopID
Order by name ASC;