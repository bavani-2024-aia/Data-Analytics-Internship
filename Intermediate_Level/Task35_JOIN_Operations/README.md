**TASK 35: JOIN Operations**



\-> JOIN is used to combine data from two or more tables.



\-> It helps retrieve related information stored in different tables.



\-> JOIN works using a common column between tables.



\-> It is useful when analyzing data spread across multiple tables.



Example:



SELECT Students.Name, Departments.DepartmentName

FROM Students

JOIN Departments

ON Students.DeptID = Departments.DeptID;



&#x20;This query displays student names along with their department names.

