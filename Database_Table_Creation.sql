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
CREATE TABLE Courses (
	ID INTEGER NOT NULL,
    Title VARCHAR(30) NOT NULL,
    Credits INTEGER NOT NULL,
    Department VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Courses PRIMARY KEY(ID)
);
CREATE TABLE Semester (
	Course_ID INTEGER NOT NULL,
    Semester VARCHAR(30) NOT NULL,
    Year INTEGER,
    CONSTRAINT PK_Semester PRIMARY KEY(Course_ID, Semester, Year),
    CONSTRAINT FK_Semester_Courses FOREIGN KEY(Course_ID) REFERENCES Courses(ID)
);
CREATE TABLE Class (
	Class_ID INTEGER NOT NULL,
    Course_ID INTEGER NOT NULL,
    Semester VARCHAR(30) NOT NULL,
    Professor_ID INTEGER NOT NULL,
    TimeDay DATETIME,
    CONSTRAINT PK_Class PRIMARY KEY(Class_ID, Course_ID, Semester),
    CONSTRAINT FK_Class_Course FOREIGN KEY(Class_ID) REFERENCES Courses(ID)
);
CREATE TABLE Attendance (
	Student_ID INTEGER NOT NULL,
    Class_ID INTEGER NOT NULL,
    Present BOOLEAN NOT NULL,
    Date TIMESTAMP NOT NULL,
    CONSTRAINT PK_Attendance PRIMARY KEY(Student_ID, Class_ID, Date),
    -- CONSTRAINT FK_Attendance_Students FOREIGN KEY(Student_ID) REFERENCES Students(Student_ID),
    CONSTRAINT FK_Attendance_Class FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)
);
