-- Script name: tests.sql
-- Author:      Rui Qi Huang
-- Purpose:     test the integrity of this database system

USE BloodDonationDB;
SET SQL_SAFE_UPDATES = 0;

-- 1. Testing appointment table
DELETE FROM Appointment WHERE user_id = 1400;
UPDATE Appointment SET location = 'Queens AVE' WHERE user_id = 6635; 

-- 2. Testing bloodtype table
DELETE FROM Blood_type WHERE blood_type = 'A';
UPDATE Blood_type SET amount = 300 WHERE gender = 'female'; 

-- 3. Testing BloodBank table
DELETE FROM BloodBank WHERE donorCount = 1;
UPDATE BloodBank SET donorCount = 300 WHERE location = 'King Drive'; 

-- 4. Testing BloodBag  table
DELETE FROM BloodBags WHERE blood_type = 'C';
UPDATE BloodBags SET amount = 300 WHERE blood_type = 'B'; 

-- 5. Testing Donors  table
DELETE FROM Donors WHERE amount = 400;
UPDATE Donors SET amount = 300 WHERE DonorID = 4; 

-- 6. Testing Exam  table
DELETE FROM Exam WHERE passed = 'true';
UPDATE Exam SET passed = 'false' WHERE idExam = 1; 

-- 7. Testing Hospitals  table
DELETE FROM Hospitals WHERE patientCount = 1;
UPDATE Hospitals SET patientCount = 300 WHERE location = 'King ave'; 

-- 8. Testing Incentive  table
DELETE FROM Incentive WHERE amount = 2;
UPDATE Incentive SET amount = 300 WHERE name = 'food'; 

-- 9. Testing Insurance  table
DELETE FROM Insurance WHERE name = '3';
UPDATE Insurance SET covered = 3 WHERE name = 'tom'; 


-- 10. Testing Inventory  table
DELETE FROM Inventory WHERE amount = 300;
UPDATE Inventory SET amount = 300 WHERE stock = 3; 


-- 11. Testing Location   table
DELETE FROM Location WHERE idLocation = 1;
UPDATE Location SET address = '1800 ave' WHERE idLocation = 2; 


-- 12. Testing Medical_device  table
DELETE FROM Medical_device WHERE idMedical_device = 2;
UPDATE Medical_device SET amount = 300 WHERE name = 'syringe'; 


-- 13. Testing Medical_Information  table
DELETE FROM Medical_Information WHERE blood_type = 'A';
UPDATE Medical_Information SET donor_patient = 'patient' WHERE name = 'Bob'; 


-- 14. Testing Reception  table
DELETE FROM Reception WHERE name = 'Aaron';
UPDATE Reception SET occupied = 'yes' WHERE phone = '5105002292'; 

-- 15. Testing Request   table
DELETE FROM Request WHERE request_id = 2;
UPDATE Request SET type = 'donor' WHERE request_id = 3; 

-- 16. Testing Supervisor  table
DELETE FROM Supervisor WHERE name = 'Aaron';
UPDATE Supervisor SET phone = '5102032' WHERE name = 'bob'; 

-- 17. Testing WalkIn   table
DELETE FROM WalkIn WHERE name = 'bobby';
UPDATE WalkIn SET gender = 'female' WHERE id = 2; 

-- 18. Testing Patients   table
DELETE FROM Patients WHERE PatientID = '4';
UPDATE Patients SET blood_type = 'A' WHERE PatientID = '4'; 

SET SQL_SAFE_UPDATES = 1;

-- SELECT * FROM Patients;