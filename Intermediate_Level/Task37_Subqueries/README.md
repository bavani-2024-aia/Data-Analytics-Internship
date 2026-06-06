**TASK 37: Subqueries**



\-> A subquery is a query written inside another SQL query.



\-> It is used to retrieve data that will be used by the main query.



\-> Subqueries help solve complex problems in a simple way.



\-> They can be used with SELECT, INSERT, UPDATE, and DELETE statements.



\-> A subquery is always enclosed within parentheses.



Example:



SELECT Name

FROM Employees

WHERE Salary > (

&#x20;   SELECT AVG(Salary)

&#x20;   FROM Employees

);



This query displays employees whose salary is greater than the average salary.

