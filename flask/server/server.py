use course_python1;
#insert into manager (name , officeID) values('Eddie' , 1);
#insert into employee (name , managerID) values('Hadas' , 1);
#insert into document(text  , employeeID) value ('SQL joins' , 1);


select office.name officeName, manager.name managerName, managerID 
from manager
join office
    on office.officeID = manager.officeID;

select employee.name employeeName, 
        manager.name managerName , 
        office.name officeName 
from employee
join manager
    on manager.managerid = employee.managerid
    join office
        on office.officeid = manager.officeID;
        
  #      update document 
  #      set text = 'OOP'
  #      where documentID = 1;
  
select text, office.name officeName , employee.name employeeName from document
join employee
    on  document.employeeID = employee.employeeID
    join manager
        on employee.managerID = manager.managerID
        join office
            on manager.officeID = office.officeID
