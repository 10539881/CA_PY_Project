
CREATE TABLE UserDetails (
UserId int IDENTITY(1,1) PRIMARY KEY,
FullName VARCHAR(100) NOT NULL,
Email VARCHAR(255) NOT NULL,
Password VARCHAR(255)
);

CREATE TABLE StudentMaster
(
StudentId int IDENTITY(1,1) PRIMARY KEY,
FirstName varchar(100) NOT NULL,
LastName varchar(100) NOT NULL,
DOB Date NOT NULL,
Country varchar(100) NOT NULL,
Mobile varchar(100) NOT NULL,
Email varchar(100) NOT NULL,
Course varchar(100) NOT NULL,
);