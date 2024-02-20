-- select name as Customers from customers
-- where id not in (select customerId from orders)


select c.name as customers from customers as c
left join orders as o
on c.id = o.customerID
where o.id is NULL
