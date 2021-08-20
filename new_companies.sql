select Emp.company_code, Cmp.founder, count(distinct lead_manager_code), count(distinct senior_manager_code), count(distinct manager_code), count(distinct employee_code)
from Employee Emp inner join Company Cmp on Emp.company_code = Cmp.company_code group by Emp.company_code, Cmp.founder order by Emp.company_code;
