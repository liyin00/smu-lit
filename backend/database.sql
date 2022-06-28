--
-- Database: "penteract_db"
--

drop database if exists penteract_db;
create database penteract_db;
use penteract_db;

--
-- Table structure for table "users"
--

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  user_id int NOT NULL AUTO_INCREMENT,
  name varchar(30) NOT NULL,
  password varchar(30) NOT NULL,
  bdae DATE NOT NULL,
  email varchar(50) NOT NULL,
  last4_nric varchar(4),
  role varchar(10) NOT NULL,
  educational_instituition varchar(50),
  study_year int,
  company varchar(50),
  position varchar(50),
  PRIMARY KEY (user_id)
);
  
--
-- Dumping data for table "users"
--

INSERT INTO users (
  user_id,
  name,
  password,
  bdae,
  email,
  last4_nric,
  role,
  educational_instituition,
  study_year,
  company,
  position
)
values (
  0,
  "Tom",
  "Tom@123",
  "1980-01-01",
  "magojc98@gmail.com",
  "123A",
  "client",
   null,
   null,
   null,
   null
),
(
  0,
  "Henry",
  "Henry@123",
  "1980-02-02",
  "magojc98@gmail.com",
   null,
  "SA",
   "Singapore Management University",
   3,
   null,
   null
),
(
  0,
  "Patrick",
  "Patrick@123",
  "1980-03-03",
  "magojc98@gmail.com",
   null,
  "lawyer",
   null,
   null,
   "Abdul Rahman Law Corporation",
   "Associate lawyer"
);
--------------------------------------------------------

-- --
-- Table structure for table "cases"
-- --

DROP TABLE IF EXISTS cases;
CREATE TABLE IF NOT EXISTS cases (
  case_id int NOT NULL AUTO_INCREMENT,
  client_name varchar(30) NOT NULL,
  client_id int NOT NULL,
  gross_salary int NOT NULL,
  case_title varchar(100) NOT NULL,
  case_category varchar(30) NOT NULL,
  court_hearing_date DATE NOT NULL,
  client_case_description varchar(1500),
  s3_url varchar(200),
  sa_id int,
  lawyer_id int,
  current_case_status varchar(30) NOT NULL,
  student_assigned_date DATE,
  case_summary_date DATE,
  finalised_case_summary_date DATE,
  confirmed_appointment_date DATE,
  consultation_date DATE,
  consultation_questions varchar(5000),
  consultation_advices varchar(5000),
  client_summary_approval varchar(30),
  pre_consult_req int,
  pre_consult_google_docs_link varchar(300),
  PRIMARY KEY (case_id)
);

--
-- Dumping data for table "cases"
--

INSERT INTO cases (
	case_id,
	client_name,
	client_id,
	gross_salary,
	case_title,
	case_category,
	court_hearing_date,
	client_case_description,
	s3_url,
	sa_id,
	lawyer_id,
	current_case_status,
	student_assigned_date,
	case_summary_date,
	finalised_case_summary_date,
	confirmed_appointment_date,
	consultation_date,
	consultation_questions,
	consultation_advices,
	client_summary_approval,
	pre_consult_req,
	pre_consult_google_docs_link
) VALUES (
	0,
	"Tom",
	1,
	2000,
    "Unhygienic food",
	"Consumer Rights",
	"2022-02-01",
	"Stall served me chicken that was dropped on the floor",
	"s3_url",
	2,
	3,
	"Active",
	"2022-01-05",
	"2022-01-10",
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL
);

-- --------------------------------------------------------

--
-- Table structure for table "case_summary"
--

DROP TABLE IF EXISTS case_summary;
CREATE TABLE IF NOT EXISTS case_summary (
  case_id int NOT NULL,
  case_summary_id int NOT NULL AUTO_INCREMENT,
  summary_of_facts varchar(3000),
  issues_questions varchar(3000),
  applicable_law varchar(2000),
  court_hearing_matter varchar(2000),
  specific_questions varchar(2000),
  client_summary_feedback varchar(1500),
  PRIMARY KEY (case_summary_id)
);

-- --------------------------------------------------------

--
-- Table structure for table "chat"
--

DROP TABLE IF EXISTS chats;
CREATE TABLE IF NOT EXISTS chats (
  case_id int NOT NULL,
  chat_id int NOT NULL AUTO_INCREMENT,
  category varchar(100) NOT NULL,
  sender_id int NOT NULL,
  message varchar(1500) NOT NULL,
  msg_date_time timestamp NOT NULL,
  PRIMARY KEY (chat_id)
);

--
-- Dumping data for table "chat"
--

INSERT INTO chats (case_id, chat_id, category, sender_id, message, msg_date_time) VALUES
(1, 0, "sa-client", "1", "Hello", CURRENT_TIMESTAMP);
-- --------------------------------------------------------

ALTER TABLE cases
  ADD CONSTRAINT cases_ibfk_1 FOREIGN KEY (client_id) REFERENCES users (user_id),
  ADD CONSTRAINT cases_ibfk_3 FOREIGN KEY (sa_id) REFERENCES users (user_id),
  ADD CONSTRAINT cases_ibfk_4 FOREIGN KEY (lawyer_id) REFERENCES users (user_id);

ALTER TABLE case_summary
  ADD CONSTRAINT case_summary_ibfk_1 FOREIGN KEY (case_id) REFERENCES cases (case_id);

ALTER TABLE chats
  ADD CONSTRAINT chat_ibfk_1 FOREIGN KEY (sender_id) REFERENCES users (user_id),
  ADD CONSTRAINT chat_ibfk_2 FOREIGN KEY (case_id) REFERENCES cases (case_id);