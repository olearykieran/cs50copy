CREATE TABLE students_update (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE house (
    id INTEGER,
    house TEXT,
    head TEXT,
    FOREIGN KEY(id)
);
CREATE TABLE connect (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    PRIMARY KEY(id)
);