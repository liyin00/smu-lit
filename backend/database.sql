--
-- Database: `penteract_db`
--

drop database if exists penteract_db;
create database penteract_db;
use penteract_db;

--------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `name` varchar(30) NOT NULL,
  `bdae` varchar(10) NOT NULL,
  `last4_nric` varchar(4) NOT NULL,
  `user_id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(10) NOT NULL,
  `study_year` int NOT NULL,
  PRIMARY KEY (`user_id`)
);

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`name`, `bdae`, `last4_nric`, `user_id`, `role`, `study_year`) VALUES
('Li Yin', '13-12-2000', '123J', 0 ,'client', 0),
('Marcus', '01-01-2020', '245A', 0, 'sa', 1),
('Amanda', '05-05-2005', '378B', 0, 'sa', 2),
('Juhi', '03-03-1993', '498C', 0, 'sl', 4),
('Gauri', '10-10-2002', '987G', 0, 'client', 0),
('Derrick', '08-08-2008', '924I', 0, 'lawyer', 0);

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `date` varchar(10) NOT NULL,
  `timeslot` int NOT NULL,
  `client_id` int NOT NULL,
  `lawyer_id` int NOT NULL,
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`appointment_id`)
);

-- --
-- -- Dumping data for table `appointment`
-- --

INSERT INTO `appointment` (`date`, `timeslot`, `client_id`, `lawyer_id`, `appointment_id`) VALUES
('28-06-2022', 15, 1, 6, 0),
('01-07-2022', 16, 5, 6, 0);

-- --------------------------------------------------------

--
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `cases`;
CREATE TABLE IF NOT EXISTS `cases` (
  `s3_url` varchar(200) NOT NULL,
  `case_id` int NOT NULL AUTO_INCREMENT,
  `case_status` varchar(30) NOT NULL,
  `case_category` varchar(30) NOT NULL,
  `hearing_date` varchar(10) NOT NULL,
  `case_title` varchar(100) NOT NULL,
  `client_case_summary` varchar(1500) NOT NULL,
  `sa_case_summary` varchar(5000) NOT NULL,
  `lawyer_case_comments` varchar(5000) NOT NULL,
  `sa_id` int NOT NULL,
  `lawyer_id` int NOT NULL,
  `client_id` int NOT NULL,
  `appointment_id` int NOT NULL,
  `client_feedback` varchar(1500) NOT NULL,
  `client_approval_status` varchar(30) NOT NULL,
  PRIMARY KEY (`case_id`)
);

--
-- Dumping data for table `cases`
--

INSERT INTO `cases` (`s3_url`, `case_id`, `case_status`, `case_category`, `hearing_date`, `case_title`, `client_case_summary`, `sa_case_summary`, `lawyer_case_comments`, `sa_id`, `lawyer_id`, `client_id`, `appointment_id`, `client_feedback`, `client_approval_status`) VALUES
('https://google.com.sg', 0, 'in progress', 'financial dispute' ,'05-07-2022', 'Dispute over inheritance after familial death', 'Father died and did not leave inheritance. Seeking a justifiable allocation of financial inheritance', 'Seeking justifable allocation of financial inheritance', 'Advice client accordingly, all in order.', 2, 6, 1, 1, 'No chance of peaceful resolvation', 'accepted');

-- --------------------------------------------------------

ALTER TABLE `cases`
  ADD CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`sa_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `cases_ibfk_2` FOREIGN KEY (`lawyer_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `cases_ibfk_3` FOREIGN KEY (`client_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `cases_ibfk_4` FOREIGN KEY (`appointment_id`) REFERENCES `appointment` (`appointment_id`);

ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`lawyer_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `users` (`user_id`);