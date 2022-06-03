select a.name as employee from employee a,employee b where a.managerId = b.id 
and a.salary>b.salary 