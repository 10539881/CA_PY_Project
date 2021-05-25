CREATE TABLE StudentMaster
(
StudentId int IDENTITY(1,1) PRIMARY KEY,
FirstName varchar(100) Not Null,
LastName varchar(100) Not Null,
DOB DateTime NOT NULL,
Country varchar(100) Not Null,
Mobile varchar(100) Not Null,
Email varchar(100) Not Null,
Course varchar(100) Not Null,
)