-- Script name: inserts.sql
-- Author:      Rui Qi Huang
-- Purpose:     sample data that represents the scope and domain of the real data that the user of the system will insert into the database

-- the database used to insert the data into.
USE BloodDonationDB;
SET FOREIGN_KEY_CHECKS=0;

-- Appointment table inserts
    INSERT INTO Appointment (date, user_id, location) VALUES (curdate(), 1400, 'Kings AVE'), (curdate(), 6635, 'Queens AVE'), (curdate(), 546, 'Joker AVE');

-- blood_type table inserts
    INSERT INTO Blood_type (blood_type, amount, gender) VALUES ('A', 200, 'male'), ('C', 100, 'female'), ('O', 300, 'male');

-- bloodbag table inserts
    INSERT INTO BloodBags (blood_type, amount, bag_id) VALUES ('B', 200, 1), ('O', 300, 2), ('C', 200, 3);

-- bloodbank table inserts
    INSERT INTO BloodBank (donorCount, inventory, location) VALUES (1, 2, "King Drive"), (1, 3, "Queen Drive"), (1, 4, "Joker Drive");

-- Donors table inserts
    INSERT INTO Donors (name, blood_type, DOB, amount, donorID) VALUES ("Tom", "C", CURDATE(), 2, 5),("Sam", "C", CURDATE(), 2, 4),("Michael", "A", CURDATE(), 2, 3); 
   
 -- Exam table inserts 
    INSERT INTO Exam (idExam, passed, length) VALUES (1, "true", 10), (2, "true", 10), (3, "false", 10);  
   
--  Hospitals table inserts 
	INSERT INTO Hospitals (patientCount, inventory, location) VALUES (1, 10, "King ave"), (1, 10, "joker ave"), (1, 10, "queen ave");

-- Incentive table inserts
	INSERT INTO Incentive (amount, inventive_id, name) VALUES (2, 10, "food"),(2, 1, "game"),(2, 3, "toy");
    
-- Insurance table inserts
	INSERT INTO Insurance (name, type, covered) VALUES ("bob", "all", "1"), ("lily", "all", "1"), ("tom", "all", "1");
		
-- Inventory table inserts
	INSERT INTO Inventory (amount, blood_type, stock) VALUES (10, "C", 3) ,(10, "O", 3),(10, "A", 3);
    
-- Location table inserts
	INSERT INTO Location (idLocation, name, address) VALUES (1, "hill drive", "1900 ave"), (2, "top drive", "1800 ave"),(3, "burney drive", "1700 ave");
    
-- medical device table inserts
	INSERT INTO Medical_device (idMedical_device, amount, name) VALUES (1, 10, "syringe"),(2, 10, "file"),(3, 10, "vial");
    
-- medical information table inserts
	INSERT INTO Medical_Information (name, blood_type, donor_patient) VALUES ("Bob", "O", "patient"), ("Cari", "O", "patient"), ("mari", "O", "patient");
    
-- patients table inserts
	INSERT INTO Patients (name, blood_type, DOB, PatientID) VALUES ("bob", "o", current_date(), "1"),("mari", "A", current_date(), "2"),("bob", "B", current_date(), "13");
    
-- reception table inserts
	INSERT INTO Reception (name, occupied, phone) VALUES ("bob", "yes", "510500500"),("cari", "yes", "510500501"),("mari", "yes", "510500200");
    
-- requests table inserts
	INSERT INTO Request (request_id, type, amount) VALUES (1, "donor", 10), (2, "donor", 10), (3, "donor", 10);
    
-- supervisor table inserts
	INSERT INTO Supervisor (name, email, phone) VALUES ("mari", "mari@gmail.com", "510520000"),("bob", "bob@gmail.com", "510504000"),("cari", "cari@gmail.com", "510500000");
    
-- walkin table inserts
	INSERT INTO WalkIn (name, gender, id) VALUES ("bobby", "male", 1), ("tom", "male", 2), ("tommy", "male", 3);

SET FOREIGN_KEY_CHECKS=1;
-- SELECT * from Hospitals;