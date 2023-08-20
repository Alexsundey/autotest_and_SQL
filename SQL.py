SELECT c.login, o.inDelivery
FROM "Couriers" AS c
RIGHT JOIN "Orders" AS o ON o.courierID = c.id;
WHERE o.inDelivery=true










SELECT o.track,
CASE
WHEN o.finished = true THEN 2
WHEN o.cancelled = true THEN -1
WHEN o.inDelivery = true THEN 1
ELSE 0
END
FROM Orders AS o;