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
  bdae DATE,
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
  'Hubert Blackburn',
  "Hubert Blackburn@123",
  "1996-06-15",
  "Hubert_Blackburn@mailinator.com",
  "501K",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Fynley Hull',
  "Fynley Hull@123",
  "1991-01-20",
  "Fynley_Hull@mailinator.com",
  "830F",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Edie Frazier',
  "Edie Frazier@123",
  "1991-10-23",
  "Edie_Frazier@mailinator.com",
  "689G",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Saoirse Lovell',
  "Saoirse Lovell@123",
  "1981-06-21",
  "Saoirse_Lovell@mailinator.com",
  "245S",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Arla Ryan',
  "Arla Ryan@123",
  "1984-09-17",
  "Arla_Ryan@mailinator.com",
  "255M",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Andrei Finney',
  "Andrei Finney@123",
  "1986-01-18",
  "Andrei_Finney@mailinator.com",
  "173R",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Stephanie Adam',
  "Stephanie Adam@123",
  "1984-09-27",
  "Stephanie_Adam@mailinator.com",
  "436T",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Samirah Horton',
  "Samirah Horton@123",
  "1995-03-25",
  "Samirah_Horton@mailinator.com",
  "311P",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Essa Ferrell',
  "Essa Ferrell@123",
  "1983-06-01",
  "Essa_Ferrell@mailinator.com",
  "656A",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Malikah Currie',
  "Malikah Currie@123",
  "1989-02-13",
  "Malikah_Currie@mailinator.com",
  "672H",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Piers Hardin',
  "Piers Hardin@123",
  "1998-02-04",
  "Piers_Hardin@mailinator.com",
  "634U",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Alissa Corona',
  "Alissa Corona@123",
  "1981-10-20",
  "Alissa_Corona@mailinator.com",
  "529E",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Ernest Beattie',
  "Ernest Beattie@123",
  "1996-08-04",
  "Ernest_Beattie@mailinator.com",
  "586G",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Cory Moss',
  "Cory Moss@123",
  "1998-09-04",
  "Cory_Moss@mailinator.com",
  "902E",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Francis Kay',
  "Francis Kay@123",
  "1991-05-01",
  "Francis_Kay@mailinator.com",
  "130E",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Mekhi Mcgrath',
  "Mekhi Mcgrath@123",
  "1997-05-05",
  "Mekhi_Mcgrath@mailinator.com",
  "762P",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Drew Finch',
  "Drew Finch@123",
  "1992-05-05",
  "Drew_Finch@mailinator.com",
  "534Q",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Nannie Owens',
  "Nannie Owens@123",
  "1986-04-07",
  "Nannie_Owens@mailinator.com",
  "125B",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Katrina Mcneil',
  "Katrina Mcneil@123",
  "1992-10-12",
  "Katrina_Mcneil@mailinator.com",
  "736P",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Katey Barclay',
  "Katey Barclay@123",
  "1988-06-16",
  "Katey_Barclay@mailinator.com",
  "266K",
  "client",
  null,
  null,
  null,
  null
),
(
  0,
  'Max Thornton',
  'Max Thornton@123',
  null,
  'Max_Thornton@mailinator.com',
  null,
  "SA",
  "Singapore Management University",
  3,
  null,
  null
),
(
  0,
  'Kaya Parker',
  'Kaya Parker@123',
  null,
  'Kaya_Parker@mailinator.com',
  null,
  "SA",
  "Singapore Management University",
  3,
  null,
  null
),
(
  0,
  'Kolby Horn',
  'Kolby Horn@123',
  null,
  'Kolby_Horn@mailinator.com',
  null,
  "SA",
  "Singapore Management University",
  3,
  null,
  null
),
(
  0,
  'Joey Burns',
  'Joey Burns@123',
  null,
  'Joey_Burns@mailinator.com',
  null,
  "SA",
  "Singapore Management University",
  3,
  null,
  null
),
(
  0,
  'Bennett Hopkins',
  'Bennett Hopkins@123',
  null,
  'Bennett_Hopkins@mailinator.com',
  null,
  "SA",
  "Singapore Management University",
  3,
  null,
  null
),
(
  0,
  "Brantley Bomgardner",
  "Brantley Bomgardner@123",
   null,
  "Brantley_Bomgardner@mailinator.com",
   null,
  "lawyer",
   null,
   null,
   "Abdul Rahman Law Corporation",
   "Associate lawyer"
),
(
  0,
  "Kimberly Burkhart",
  "Kimberly Burkhart@123",
   null,
  "Kimberly_Burkhart@mailinator.com",
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
  case_category varchar(1000) NOT NULL,
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
  summary_key_words varchar(1000),
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
	summary_key_words
) VALUES (
  0,
  'Hubert Blackburn',
  1,
  2000,
  'Claiming insurance for car accident',
  'Claims',
  '2022-11-22',
  'client_case_description_here',
  'www.google.com',
  NULL,
  NULL,
  'New Case',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Fynley Hull',
  2,
  2000,
  'Unfair splitting of assets with Yi Loh Ping',
  'Division of Property',
  '2022-11-15',
  'client_case_description_here',
  'www.google.com',
  NULL,
  NULL,
  'New Case',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Edie Frazier',
  3,
  2000,
  'Tenant refused to pay rent',
  'Basic Advice on Tenancy Issue',
  '2022-08-17',
  'client_case_description_here',
  'www.google.com',
  NULL,
  NULL,
  'New Case',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Saoirse Lovell',
  4,
  2000,
  'Request for protection from emotionally and physically abusive ex-boyfriend ',
  'Personal Protection Order',
  '2022-09-25',
  'client_case_description_here',
  'www.google.com',
  NULL,
  NULL,
  'New Case',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Arla Ryan',
  5,
  2000,
  'Protection required from violent husband',
  'Personal Protection Order',
  '2022-12-17',
  'client_case_description_here',
  'www.google.com',
  NULL,
  NULL,
  'New Case',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Andrei Finney',
  6,
  2000,
  'Custody of Son',
  'Custody of Children',
  '2022-08-25',
  'client_case_description_here',
  'www.google.com',
  24,
  25,
  'Assigned cases',
  '2022-06-20',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Stephanie Adam',
  7,
  2000,
  'Accessing property under the name of late husband',
  'Probate (Estate Matters)',
  '2022-08-22',
  'client_case_description_here',
  'www.google.com',
  23,
  27,
  'Assigned cases',
  '2022-06-25',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Samirah Horton',
  8,
  2000,
  'Employer fired me for watching cat videos',
  'Employment Issue',
  '2022-08-25',
  'client_case_description_here',
  'www.google.com',
  24,
  26,
  'Assigned cases',
  '2022-06-25',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Essa Ferrell',
  9,
  2000,
  'Custody of Koh',
  'Custody of Children',
  '2022-07-23',
  'client_case_description_here',
  'www.google.com',
  22,
  26,
  'Assigned cases',
  '2022-06-27',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Malikah Currie',
  10,
  2000,
  'Cheating husband',
  'Divorce',
  '2022-07-25',
  'client_case_description_here',
  'www.google.com',
  24,
  27,
  'Assigned cases',
  '2022-06-22',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL
),
(
  0,
  'Piers Hardin',
  11,
  2000,
  'Violent Wife',
  'Personal Protection Order',
  '2022-07-21',
  'client_case_description_here',
  'www.google.com',
  22,
  26,
  'Active',
  '2022-06-26',
  '2022-06-28',
  '2022-06-29',
  NULL,
  NULL,
  NULL,
  NULL,
  1,
  NULL,
  NULL
),
(
  0,
  'Alissa Corona',
  12,
  2000,
  'Monthly allowance from ex-husband',
  'Claims for Maintenance',
  '2022-07-18',
  'client_case_description_here',
  'www.google.com',
  24,
  27,
  'Active',
  '2022-06-27',
  '2022-06-28',
  '2022-06-30',
  NULL,
  NULL,
  NULL,
  NULL,
  1,
  NULL,
  NULL
),
(
  0,
  'Ernest Beattie',
  13,
  2000,
  "Splitting assets among siblings after father's sudden passing",
  'Probate (Estate Matters)',
  '2022-07-16',
  'client_case_description_here',
  'www.google.com',
  21,
  27,
  'Active',
  '2022-06-26',
  '2022-06-27',
  '2022-06-30',
  NULL,
  NULL,
  NULL,
  NULL,
  1,
  NULL,
  NULL
),
(
  0,
  'Cory Moss',
  14,
  2000,
  'Smoking Contraband Cigarettes',
  'Basic Advice on Criminal Matters',
  '2022-03-28',
  'client_case_description_here',
  'www.google.com',
  22,
  26,
  'Closed',
  '2022-03-15',
  '2022-03-17',
  '2022-03-21',
  '2022-03-23',
  '2022-03-25',
  NULL,
  NULL,
  1,
  NULL,
  'custom,litigate,legalize,breach,voluntary,void,nephew,lex,verboten,decretal'
),
(
  0,
  'Francis Kay',
  15,
  2000,
  'Terminating Lease Agreement in COVID-19',
  'Basic Advice on Tenancy Issue',
  '2022-03-27',
  'client_case_description_here',
  'www.google.com',
  21,
  27,
  'Closed',
  '2022-03-13',
  '2022-03-15',
  '2022-03-17',
  '2022-03-21',
  '2022-03-23',
  NULL,
  NULL,
  1,
  NULL,
  'in,divan,mandator,appendant,juridical,wrong,interdict,summons,relation,law'
),
(
  0,
  'Mekhi Mcgrath',
  16,
  2000,
  'Speeding ticket while driving pregnant wife to the hospital',
  'Basic Advice on Traffic Offences',
  '2022-03-19',
  'client_case_description_here',
  'www.google.com',
  23,
  27,
  'Closed',
  '2022-02-28',
  '2022-03-01',
  '2022-03-07',
  '2022-03-13',
  '2022-03-15',
  NULL,
  NULL,
  1,
  NULL,
  'forensic,Rutherford,legal,Mariotte,heteronomous,restriction,tacit,nomos,deem,joinder     '
),
(
  0,
  'Drew Finch',
  17,
  2000,
  'Request for protection from emotionally and physically abusive ex-girlfriend',
  'Personal Protection Order',
  '2022-03-15',
  'client_case_description_here',
  'www.google.com',
  24,
  26,
  'Closed',
  '2022-02-23',
  '2022-02-27',
  '2022-03-01',
  '2022-03-05',
  '2022-03-07',
  NULL,
  NULL,
  1,
  NULL,
  'mitzvah,law,demur,ecclesiastical,reply,retrial,status,passage,principle,jurisconsult     '
),
(
  0,
  'Nannie Owens',
  18,
  2000,
  'I got fired!!!',
  'Employment Issue',
  '2022-02-28',
  'client_case_description_here',
  'www.google.com',
  22,
  26,
  'Closed',
  '2022-02-11',
  '2022-02-13',
  '2022-02-17',
  '2022-02-21',
  '2022-02-24',
  NULL,
  NULL,
  1,
  NULL,
  'admiralty,jus,illegal,civilian,voluntary,servitus,rule,Mendeléeff,advantage,trespass     '
),
(
  0,
  'Katrina Mcneil',
  19,
  2000,
  'Underage smoking',
  'Basic Advice on Criminal Matters',
  '2022-05-17',
  'client_case_description_here',
  'www.google.com',
  21,
  26,
  'Closed',
  '2022-05-01',
  '2022-05-03',
  '2022-05-05',
  '2022-05-11',
  '2022-05-13',
  NULL,
  NULL,
  1,
  NULL,
  'statute,sentence,sequester,daughter,convey,nomocracy,statutory,dispense,general,uncharged'
),
(
  0,
  'Katey Barclay',
  20,
  2000,
  'Accessing property under the name of late husband ',
  'Division of Property',
  '2022-06-05',
  'client_case_description_here',
  'www.google.com',
  24,
  27,
  'Closed',
  '2022-06-01',
  '2022-06-25',
  '2022-05-27',
  '2022-06-01',
  '2022-06-05',
  NULL,
  NULL,
  1,
  NULL,
  'criminally,constitute,SIL,law,antinomy,ordinance,stand,good,sequestration,legitimate'
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
  
select* from cases;