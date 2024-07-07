-- Example SQL schema definition
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Age INT,
    Gender NVARCHAR(10)
    -- Add more columns as needed
);

CREATE TABLE Treatments (
    TreatmentID INT PRIMARY KEY,
    PatientID INT,
    TreatmentDate DATE,
    TreatmentType NVARCHAR(50),
    Outcome NVARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
    -- Add more columns as needed
);
