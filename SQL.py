SELECT c.login, COUNT(o.courierId) AS delivered_orders
FROM "Couriers" AS c
JOIN "Orders" AS o ON o.courierID = c.id;
WHERE o.inDelivery=true
GROUP BY c.login;









SELECT o.track,
CASE
WHEN o.finished = true THEN 2
WHEN o.cancelled = true THEN -1
WHEN o.inDelivery = true THEN 1
ELSE 0
END
FROM Orders AS o;