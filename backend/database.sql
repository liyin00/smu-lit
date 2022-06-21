-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 08, 2021 at 06:37 PM
-- Server version: 8.0.18
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cf1`
--

-- --------------------------------------------------------

--
-- Table structure for table `badges`
--

DROP TABLE IF EXISTS `badges`;
CREATE TABLE IF NOT EXISTS `badges` (
  `employeeName` varchar(100) NOT NULL,
  `badges` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  PRIMARY KEY (`employeeName`,`badges`,`cohortName`),
  KEY `badges` (`badges`,`cohortName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `badges`
--

INSERT INTO `badges` (`employeeName`, `badges`, `cohortName`) VALUES
('Teller', 'Introduction to flask', 'G0'),
('Teller', 'Introduction to HTML', 'G0'),
('Teller', 'Introduction to life', 'G0'),
('Bob', 'Introduction to life', 'G1'),
('Teller', 'Introduction to python', 'G0');

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

DROP TABLE IF EXISTS `chapter`;
CREATE TABLE IF NOT EXISTS `chapter` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `graded` int(11) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`,`chapterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `chapter`
--

INSERT INTO `chapter` (`courseName`, `cohortName`, `chapterID`, `duration`, `graded`) VALUES
('Introduction to life', 'G1', -1, 2, 1),
('Introduction to life', 'G1', 1, 2, 0),
('Introduction to life', 'G1', 2, 1, 0),
('Introduction to life', 'G1', 3, 1, 0),
('Introduction to life', 'G1', 4, 1, 0),
('Introduction to life', 'G1', 5, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `cohort`
--

DROP TABLE IF EXISTS `cohort`;
CREATE TABLE IF NOT EXISTS `cohort` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `enrollmentStartDate` varchar(30) NOT NULL,
  `enrollmentStartTime` varchar(30) NOT NULL,
  `enrollmentEndDate` varchar(30) NOT NULL,
  `enrollmentEndTime` varchar(30) NOT NULL,
  `cohortStartDate` varchar(30) NOT NULL,
  `cohortStartTime` varchar(30) NOT NULL,
  `cohortEndDate` varchar(30) NOT NULL,
  `cohortEndTime` varchar(30) NOT NULL,
  `trainerName` varchar(100) NOT NULL,
  `cohortSize` int(11) NOT NULL,
  `slotLeft` int(11) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`),
  KEY `trainerName` (`trainerName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cohort`
--

INSERT INTO `cohort` (`courseName`, `cohortName`, `enrollmentStartDate`, `enrollmentStartTime`, `enrollmentEndDate`, `enrollmentEndTime`, `cohortStartDate`, `cohortStartTime`, `cohortEndDate`, `cohortEndTime`, `trainerName`, `cohortSize`, `slotLeft`) VALUES
('Big questions', 'G1', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 30),
('Finance and accounting', 'G1', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to flask', 'G0', '01 Feb 2021', '00:00', '28 Feb 2021', '23:59', '01 May 2021', '08:00', '30 May 2021', '20:00', 'Vera', 30, 4),
('Introduction to flask', 'G1', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to HTML', 'G0', '08 Sep 2021', '00:00', '28 Sep 2021', '23:59', '01 Oct 2021', '08:00', '10 Oct 2021', '20:00', 'Charles', 30, 9),
('Introduction to HTML', 'G1', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to HTML', 'G2', '08 Oct 2021', '00:00', '18 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to HTML', 'G3', '18 Oct 2021', '00:00', '28 Oct 2021', '23:59', '10 Nov 2021', '08:00', '20 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to HTML', 'G4', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '10 Nov 2021', '08:00', '20 Nov 2021', '20:00', 'Charles', 30, 30),
('Introduction to life', 'G0', '01 Sep 1998', '00:00', '28 Oct 1998', '23:59', '01 Nov 1998', '08:00', '30 Nov 1998', '20:00', 'Marcus', 30, 5),
('Introduction to life', 'G1', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 25),
('Introduction to python', 'G0', '08 Oct 2019', '00:00', '28 Oct 2019', '23:59', '01 Nov 2019', '08:00', '30 Nov 2019', '20:00', 'Charles', 30, 10),
('Introduction to python', 'G1', '08 Oct 1998', '00:00', '28 Oct 1998', '23:59', '01 Nov 1998', '08:00', '30 Nov 1998', '20:00', 'Charles', 30, 30),
('Introduction to python', 'G2', '08 Oct 2019', '00:00', '28 Oct 2019', '23:59', '01 Nov 2019', '08:00', '30 Nov 2019', '20:00', 'Charles', 30, 30),
('Introduction to python', 'G3', '08 Oct 2021', '00:00', '28 Oct 2021', '23:59', '01 Nov 2021', '08:00', '30 Nov 2021', '20:00', 'Charles', 30, 24);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `courseName` varchar(100) NOT NULL,
  `courseImage` varchar(100) NOT NULL,
  `courseDescription` varchar(200) NOT NULL,
  `prerequisite` varchar(500) NOT NULL,
  PRIMARY KEY (`courseName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`courseName`, `courseImage`, `courseDescription`, `prerequisite`) VALUES
('Big questions', 'images/course_4.jpg', 'This course introduces learners to the biggest questions in life', 'Finance and accounting'),
('Finance and accounting', 'images/course_3.jpg', 'This course introduces learners to the world of money', 'Introduction to HTML'),
('Introduction to flask', 'images/course_5.jpg', 'This course introduces learners to the flask langauge', ''),
('Introduction to HTML', 'images/course_2.jpg', 'This course introduces learners to HTML', 'Introduction to python'),
('Introduction to life', 'images/course_6.jpg', 'This course introduces learners to life', ''),
('Introduction to python', 'images/course_1.jpg', 'This course introduces learners to the python langauge', '');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `employeeName` varchar(100) NOT NULL,
  `userName` varchar(100) NOT NULL,
  `currentDesignation` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`employeeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employeeName`, `userName`, `currentDesignation`, `department`) VALUES
('Adele', 'Adele_03', 'Learner', 'Operations'),
('Alice', 'Alice_01', 'Admin', 'HR'),
('Beyonce', 'Beyonce_03', 'Learner', 'Operations'),
('Bob', 'Bob_03', 'Learner', 'Operations'),
('Brandy', 'Brandy_03', 'Learner', 'Operations'),
('Britney', 'Britney_03', 'Learner', 'Operations'),
('Charles', 'Charles_02', 'trainer', 'Operations'),
('Cher', 'Cher_03', 'Learner', 'Operations'),
('Drake', 'Drake_03', 'Learner', 'Operations'),
('Elvis', 'Elvis_03', 'Learner', 'Operations'),
('Madonna', 'Madonna_03', 'Learner', 'Operations'),
('Marcus', 'Marcus_02', 'trainer', 'Operations'),
('Prince', 'Prince_03', 'Learner', 'Operations'),
('Rihanna', 'Rihanna_03', 'Learner', 'Operations'),
('Selena', 'Selena_03', 'Learner', 'Operations'),
('Shakira', 'Shakira_03', 'Learner', 'Operations'),
('Teller', 'Teller_03', 'Learner', 'Operations'),
('Usher', 'Usher_03', 'Learner', 'Operations'),
('Vera', 'Vera_02', 'trainer', 'Operations');

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

DROP TABLE IF EXISTS `enrollment`;
CREATE TABLE IF NOT EXISTS `enrollment` (
  `employeeName` varchar(100) NOT NULL,
  `courseNameEnrolled` varchar(100) NOT NULL,
  `cohortNameEnrolled` varchar(100) NOT NULL,
  `recent` int(11) NOT NULL,
  PRIMARY KEY (`employeeName`,`courseNameEnrolled`,`cohortNameEnrolled`),
  KEY `courseNameEnrolled` (`courseNameEnrolled`,`cohortNameEnrolled`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`employeeName`, `courseNameEnrolled`, `cohortNameEnrolled`, `recent`) VALUES
('Adele', 'Introduction to life', 'G1', 1),
('Adele', 'Introduction to python', 'G3', 1),
('Bob', 'Introduction to python', 'G3', 1),
('Brandy', 'Introduction to life', 'G1', 1),
('Brandy', 'Introduction to python', 'G3', 1),
('Britney', 'Introduction to life', 'G1', 1),
('Britney', 'Introduction to python', 'G3', 1),
('Madonna', 'Introduction to life', 'G1', 1),
('Madonna', 'Introduction to python', 'G3', 1),
('Shakira', 'Introduction to python', 'G3', 1);

-- --------------------------------------------------------

--
-- Table structure for table `enrollmentrequest`
--

DROP TABLE IF EXISTS `enrollmentrequest`;
CREATE TABLE IF NOT EXISTS `enrollmentrequest` (
  `courseNameRequest` varchar(100) NOT NULL,
  `cohortNameRequest` varchar(100) NOT NULL,
  `learnerName` varchar(100) NOT NULL,
  PRIMARY KEY (`courseNameRequest`,`cohortNameRequest`,`learnerName`),
  KEY `learnerName` (`learnerName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `enrollmentrequest`
--

INSERT INTO `enrollmentrequest` (`courseNameRequest`, `cohortNameRequest`, `learnerName`) VALUES
('Introduction to life', 'G1', 'Shakira');

-- --------------------------------------------------------

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
CREATE TABLE IF NOT EXISTS `materials` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `materialURL` varchar(100) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`,`chapterID`,`materialID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `materials`
--

INSERT INTO `materials` (`courseName`, `cohortName`, `chapterID`, `materialID`, `materialURL`) VALUES
('Introduction to life', 'G1', -1, 0, '0'),
('Introduction to life', 'G1', 1, 1, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week1a-Introduction.pdf'),
('Introduction to life', 'G1', 1, 2, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week1b-SPM-fundamentals-G3-shared.pdf'),
('Introduction to life', 'G1', 1, 3, 'https://spmprojectlearnermaterials.s3.amazonaws.com/What+is+agile.mp4'),
('Introduction to life', 'G1', 2, 1, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week2-SWDevProcess-G3.pdf'),
('Introduction to life', 'G1', 2, 2, 'https://spmprojectlearnermaterials.s3.amazonaws.com/What+is+Scrum.mp4'),
('Introduction to life', 'G1', 3, 1, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week3a-UserStoryExercise-Student.pdf'),
('Introduction to life', 'G1', 4, 1, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week3b-PairProgrammingExercise.pdf'),
('Introduction to life', 'G1', 5, 1, 'https://spmprojectlearnermaterials.s3.amazonaws.com/Week4-DesignExercise2.pdf'),
('Introduction to life', 'G1', 5, 2, 'https://spmprojectlearnermaterials.s3.amazonaws.com/GitHub+Actions+in+under+1+minute!.mp4');

-- --------------------------------------------------------

--
-- Table structure for table `materialstatus`
--

DROP TABLE IF EXISTS `materialstatus`;
CREATE TABLE IF NOT EXISTS `materialstatus` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `materialID` int(11) NOT NULL,
  `employeeName` varchar(100) NOT NULL,
  `done` int(11) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`,`chapterID`,`materialID`,`employeeName`),
  KEY `employeeName` (`employeeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `materialstatus`
--

INSERT INTO `materialstatus` (`courseName`, `cohortName`, `chapterID`, `materialID`, `employeeName`, `done`) VALUES
('Introduction to life', 'G1', -1, 0, 'Adele', 0),
('Introduction to life', 'G1', -1, 0, 'Bob', 0),
('Introduction to life', 'G1', -1, 0, 'Brandy', 0),
('Introduction to life', 'G1', -1, 0, 'Britney', 0),
('Introduction to life', 'G1', -1, 0, 'Madonna', 0),
('Introduction to life', 'G1', 1, 1, 'Adele', 0),
('Introduction to life', 'G1', 1, 1, 'Bob', 1),
('Introduction to life', 'G1', 1, 1, 'Brandy', 0),
('Introduction to life', 'G1', 1, 1, 'Britney', 0),
('Introduction to life', 'G1', 1, 1, 'Madonna', 0),
('Introduction to life', 'G1', 1, 2, 'Adele', 0),
('Introduction to life', 'G1', 1, 2, 'Bob', 1),
('Introduction to life', 'G1', 1, 2, 'Brandy', 0),
('Introduction to life', 'G1', 1, 2, 'Britney', 0),
('Introduction to life', 'G1', 1, 2, 'Madonna', 0),
('Introduction to life', 'G1', 1, 3, 'Adele', 0),
('Introduction to life', 'G1', 1, 3, 'Bob', 1),
('Introduction to life', 'G1', 1, 3, 'Brandy', 0),
('Introduction to life', 'G1', 1, 3, 'Britney', 0),
('Introduction to life', 'G1', 1, 3, 'Madonna', 0),
('Introduction to life', 'G1', 2, 1, 'Adele', 0),
('Introduction to life', 'G1', 2, 1, 'Bob', 1),
('Introduction to life', 'G1', 2, 1, 'Brandy', 0),
('Introduction to life', 'G1', 2, 1, 'Britney', 0),
('Introduction to life', 'G1', 2, 1, 'Madonna', 0),
('Introduction to life', 'G1', 2, 2, 'Adele', 0),
('Introduction to life', 'G1', 2, 2, 'Bob', 1),
('Introduction to life', 'G1', 2, 2, 'Brandy', 0),
('Introduction to life', 'G1', 2, 2, 'Britney', 0),
('Introduction to life', 'G1', 2, 2, 'Madonna', 0),
('Introduction to life', 'G1', 3, 1, 'Adele', 0),
('Introduction to life', 'G1', 3, 1, 'Bob', 1),
('Introduction to life', 'G1', 3, 1, 'Brandy', 0),
('Introduction to life', 'G1', 3, 1, 'Britney', 0),
('Introduction to life', 'G1', 3, 1, 'Madonna', 0),
('Introduction to life', 'G1', 4, 1, 'Adele', 0),
('Introduction to life', 'G1', 4, 1, 'Bob', 1),
('Introduction to life', 'G1', 4, 1, 'Brandy', 0),
('Introduction to life', 'G1', 4, 1, 'Britney', 0),
('Introduction to life', 'G1', 4, 1, 'Madonna', 0),
('Introduction to life', 'G1', 5, 1, 'Adele', 0),
('Introduction to life', 'G1', 5, 1, 'Bob', 1),
('Introduction to life', 'G1', 5, 1, 'Brandy', 0),
('Introduction to life', 'G1', 5, 1, 'Britney', 0),
('Introduction to life', 'G1', 5, 1, 'Madonna', 0),
('Introduction to life', 'G1', 5, 2, 'Adele', 0),
('Introduction to life', 'G1', 5, 2, 'Bob', 1),
('Introduction to life', 'G1', 5, 2, 'Brandy', 0),
('Introduction to life', 'G1', 5, 2, 'Britney', 0),
('Introduction to life', 'G1', 5, 2, 'Madonna', 0);

-- --------------------------------------------------------

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
CREATE TABLE IF NOT EXISTS `options` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `optionID` int(11) NOT NULL,
  `optionText` varchar(300) NOT NULL,
  `isRight` int(11) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`,`chapterID`,`questionID`,`optionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `options`
--

INSERT INTO `options` (`courseName`, `cohortName`, `chapterID`, `questionID`, `optionID`, `optionText`, `isRight`) VALUES
('Introduction to life', 'G1', -1, 1, 1, 'True', 1),
('Introduction to life', 'G1', -1, 1, 2, 'False', 0),
('Introduction to life', 'G1', -1, 2, 1, '910', 0),
('Introduction to life', 'G1', -1, 2, 2, '19', 1),
('Introduction to life', 'G1', -1, 2, 3, '21', 0),
('Introduction to life', 'G1', 1, 1, 1, 'img', 1),
('Introduction to life', 'G1', 1, 1, 2, 'pic', 0),
('Introduction to life', 'G1', 1, 1, 3, 'photo', 0),
('Introduction to life', 'G1', 1, 2, 1, 'True', 1),
('Introduction to life', 'G1', 1, 2, 2, 'False', 0),
('Introduction to life', 'G1', 1, 3, 1, 'True', 0),
('Introduction to life', 'G1', 1, 3, 2, 'False', 1),
('Introduction to life', 'G1', 2, 1, 1, 'IS212', 1),
('Introduction to life', 'G1', 2, 1, 2, 'IS222', 0),
('Introduction to life', 'G1', 2, 1, 3, 'IS232', 0),
('Introduction to life', 'G1', 3, 1, 1, 'True', 0),
('Introduction to life', 'G1', 3, 1, 2, 'False', 1),
('Introduction to life', 'G1', 4, 1, 1, 'Subhajit', 0),
('Introduction to life', 'G1', 4, 1, 2, 'Kankan', 0),
('Introduction to life', 'G1', 4, 1, 3, 'Chris', 1),
('Introduction to life', 'G1', 5, 1, 1, 'True', 1),
('Introduction to life', 'G1', 5, 1, 2, 'False', 0);

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE TABLE IF NOT EXISTS `question` (
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `questionText` varchar(300) NOT NULL,
  PRIMARY KEY (`courseName`,`cohortName`,`chapterID`,`questionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`courseName`, `cohortName`, `chapterID`, `questionID`, `questionText`) VALUES
('Introduction to life', 'G1', -1, 1, 'This is the final quiz'),
('Introduction to life', 'G1', -1, 2, 'what is 9+10?'),
('Introduction to life', 'G1', 1, 1, 'Which of the following is an image tag?'),
('Introduction to life', 'G1', 1, 2, 'The team is made up of 5 members'),
('Introduction to life', 'G1', 1, 3, 'Meetings are through microsoft teams'),
('Introduction to life', 'G1', 2, 1, 'what is the code for spm?'),
('Introduction to life', 'G1', 3, 1, 'SPM class is on a Thursday'),
('Introduction to life', 'G1', 4, 1, 'Who is not our prof?'),
('Introduction to life', 'G1', 5, 1, 'Man United is the best football club in the world');

-- --------------------------------------------------------

--
-- Table structure for table `userattempt`
--

DROP TABLE IF EXISTS `userattempt`;
CREATE TABLE IF NOT EXISTS `userattempt` (
  `employeeName` varchar(100) NOT NULL,
  `courseName` varchar(100) NOT NULL,
  `cohortName` varchar(100) NOT NULL,
  `chapterID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `choiceID` int(11) NOT NULL,
  `marks` int(11) NOT NULL,
  PRIMARY KEY (`employeeName`,`courseName`,`cohortName`,`chapterID`,`questionID`),
  KEY `courseName` (`courseName`,`cohortName`,`chapterID`,`questionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userattempt`
--

INSERT INTO `userattempt` (`employeeName`, `courseName`, `cohortName`, `chapterID`, `questionID`, `choiceID`, `marks`) VALUES
('Bob', 'Introduction to life', 'G1', -1, 1, 1, 1),
('Bob', 'Introduction to life', 'G1', -1, 2, 2, 1),
('Bob', 'Introduction to life', 'G1', 1, 1, -1, 1),
('Bob', 'Introduction to life', 'G1', 1, 2, -1, 1),
('Bob', 'Introduction to life', 'G1', 1, 3, -1, 1),
('Bob', 'Introduction to life', 'G1', 2, 1, 3, 1),
('Bob', 'Introduction to life', 'G1', 3, 1, -1, 1),
('Bob', 'Introduction to life', 'G1', 4, 1, 3, 1),
('Bob', 'Introduction to life', 'G1', 5, 1, 1, 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `badges`
--
ALTER TABLE `badges`
  ADD CONSTRAINT `badges_ibfk_1` FOREIGN KEY (`employeeName`) REFERENCES `employee` (`employeeName`),
  ADD CONSTRAINT `badges_ibfk_2` FOREIGN KEY (`badges`,`cohortName`) REFERENCES `cohort` (`courseName`, `cohortName`);

--
-- Constraints for table `chapter`
--
ALTER TABLE `chapter`
  ADD CONSTRAINT `chapter_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`) REFERENCES `cohort` (`courseName`, `cohortName`);

--
-- Constraints for table `cohort`
--
ALTER TABLE `cohort`
  ADD CONSTRAINT `cohort_ibfk_1` FOREIGN KEY (`courseName`) REFERENCES `course` (`courseName`),
  ADD CONSTRAINT `cohort_ibfk_2` FOREIGN KEY (`trainerName`) REFERENCES `employee` (`employeeName`);

--
-- Constraints for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`employeeName`) REFERENCES `employee` (`employeeName`),
  ADD CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`courseNameEnrolled`,`cohortNameEnrolled`) REFERENCES `cohort` (`courseName`, `cohortName`);

--
-- Constraints for table `enrollmentrequest`
--
ALTER TABLE `enrollmentrequest`
  ADD CONSTRAINT `enrollmentrequest_ibfk_1` FOREIGN KEY (`courseNameRequest`,`cohortNameRequest`) REFERENCES `cohort` (`courseName`, `cohortName`),
  ADD CONSTRAINT `enrollmentrequest_ibfk_2` FOREIGN KEY (`learnerName`) REFERENCES `employee` (`employeeName`);

--
-- Constraints for table `materials`
--
ALTER TABLE `materials`
  ADD CONSTRAINT `materials_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`,`chapterID`) REFERENCES `chapter` (`courseName`, `cohortName`, `chapterID`);

--
-- Constraints for table `materialstatus`
--
ALTER TABLE `materialstatus`
  ADD CONSTRAINT `materialstatus_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`,`chapterID`,`materialID`) REFERENCES `materials` (`courseName`, `cohortName`, `chapterID`, `materialID`),
  ADD CONSTRAINT `materialstatus_ibfk_2` FOREIGN KEY (`employeeName`) REFERENCES `employee` (`employeeName`);

--
-- Constraints for table `options`
--
ALTER TABLE `options`
  ADD CONSTRAINT `options_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`,`chapterID`,`questionID`) REFERENCES `question` (`courseName`, `cohortName`, `chapterID`, `questionID`);

--
-- Constraints for table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`,`chapterID`) REFERENCES `chapter` (`courseName`, `cohortName`, `chapterID`);

--
-- Constraints for table `userattempt`
--
ALTER TABLE `userattempt`
  ADD CONSTRAINT `userattempt_ibfk_1` FOREIGN KEY (`courseName`,`cohortName`,`chapterID`,`questionID`) REFERENCES `question` (`courseName`, `cohortName`, `chapterID`, `questionID`),
  ADD CONSTRAINT `userattempt_ibfk_2` FOREIGN KEY (`employeeName`) REFERENCES `employee` (`employeeName`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
