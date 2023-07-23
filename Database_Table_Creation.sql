DROP TABLE IF EXISTS Students, Professors, Courses, Semester, Class, Attendance;
CREATE TABLE Students (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    First_Name VARCHAR(30),
    Last_Name VARCHAR(30),
    Gender CHAR(1),
    Email VARCHAR(30) NOT NULL,
    Address VARCHAR(80) NOT NULL,
    Credits INTEGER,
    Status VARCHAR(20),
    Major VARCHAR(20),
    CONSTRAINT PK_Students PRIMARY KEY(ID)
);
ALTER TABLE Students AUTO_INCREMENT = 910000001;
INSERT INTO Students(First_Name, Last_Name, Gender, Email, Address, Credits, Status, Major) VALUES
	("Arvindh", "Velrajan", 'M', "tun67213@temple.edu", "random", 12, "Part Time", "Computer Science");
CREATE TABLE Professors (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    First_Name VARCHAR(30),
    Last_Name VARCHAR(30),
    Email VARCHAR(30) NOT NULL,
    Dept VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Professors PRIMARY KEY(ID)
);
ALTER TABLE Professors AUTO_INCREMENT = 1;
INSERT INTO Professors(First_Name, Last_Name, Email, Dept) VALUES
	("Big", "Brain", "bigbrain@temple.edu", "Computer Science");
CREATE TABLE Courses (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    Title VARCHAR(30) NOT NULL,
    Credits INTEGER NOT NULL,
    Department VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Courses PRIMARY KEY(ID)
);
ALTER TABLE Courses AUTO_INCREMENT = 1;
INSERT INTO Courses(Title, Credits, Department) VALUES
	("Database Management", 4, "Computer Science");
CREATE TABLE Semester (
	Semester_ID INTEGER NOT NULL AUTO_INCREMENT,
    Semester VARCHAR(30) NOT NULL,
    Offered_Year INTEGER,
    CONSTRAINT PK_Semester PRIMARY KEY(Semester_ID)
);
ALTER TABLE Semester AUTO_INCREMENT = 1;
INSERT INTO Semester(Semester, Offered_Year) VALUES
	("Spring", "2023");

CREATE TABLE Class (
	Class_ID INTEGER NOT NULL AUTO_INCREMENT,
    Semester_ID INTEGER NOT NULL,
	Course_ID INTEGER NOT NULL,
    Professor_ID INTEGER NOT NULL,
    Days VARCHAR(10) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CONSTRAINT PK_Class PRIMARY KEY(Class_ID),
    CONSTRAINT FK_Class_Course FOREIGN KEY(Course_ID) REFERENCES Courses(ID),
    CONSTRAINT FK_Class_Semester_ID FOREIGN KEY(Semester_ID) REFERENCES Semester(Semester_ID),
    CONSTRAINT FK_Class_Professor_ID FOREIGN KEY(Professor_ID) REFERENCES Professors(ID)
);
ALTER TABLE Class AUTO_INCREMENT = 1;
INSERT INTO Class(Semester_ID, Course_ID, Professor_ID, Days, StartTime, EndTime) VALUES
	(1, 1, 1, "MWF", "10:00", "11:00");
CREATE TABLE Attendance (
	Student_ID INTEGER NOT NULL,
    Class_ID INTEGER NOT NULL,
    Present BOOLEAN NOT NULL,
    DateOf TIMESTAMP NOT NULL,
    CONSTRAINT PK_Attendance PRIMARY KEY(Student_ID, Class_ID, DateOf),
    -- CONSTRAINT FK_Attendance_Students FOREIGN KEY(Student_ID) REFERENCES Students(Student_ID),
    CONSTRAINT FK_Attendance_Class FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)
);
