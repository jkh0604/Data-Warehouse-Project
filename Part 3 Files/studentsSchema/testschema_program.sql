-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: testschema
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `program`
--

DROP TABLE IF EXISTS `program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `program` (
  `CollegeID` varchar(5) GENERATED ALWAYS AS (concat(left(`Major`,2),_utf8mb4'',`Degree`)) STORED NOT NULL,
  `College` varchar(45) GENERATED ALWAYS AS ((case when (`Major` in (_utf8mb4'Computer Sc',_utf8mb4'Info Sc',_utf8mb4'Applied Sc')) then _utf8mb4'Cyber College' when (`Major` in (_utf8mb4'Accounting',_utf8mb4'B Admin',_utf8mb4'Economics')) then _utf8mb4'College of Business' when (`Major` in (_utf8mb4'Elementary',_utf8mb4'Secondary')) then _utf8mb4'College of Education' when (`Major` in (_utf8mb4'Biology',_utf8mb4'Chemistry')) then _utf8mb4'College of Art and Science' end)) STORED,
  `Major` varchar(45) DEFAULT NULL,
  `Degree` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CollegeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program`
--

LOCK TABLES `program` WRITE;
/*!40000 ALTER TABLE `program` DISABLE KEYS */;
INSERT INTO `program` (`Major`, `Degree`) VALUES ,'Accounting','BA'),,'Accounting','BA'),'Applied Sc','MS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),'Elementary','EdD'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),'Elementary','EdD'),'Elementary','MS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),'Elementary','EdD'),'Elementary','MS'),'Info Sc','BS'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),'Elementary','EdD'),'Elementary','MS'),'Info Sc','BS'),'Secondary','EdD'),,'Accounting','BA'),'Applied Sc','MS'),'Applied Sc','PhD'),'B Admin','BA'),'B Admin','MBA'),'Biology','AS'),'Biology','BS'),'Biology','MS'),'Chemistry','AS'),'Chemistry','BS'),'Chemistry','MS'),'Computer Sc','AS'),'Computer Sc','BS'),'Computer Sc','MS'),'Computer Sc','PhD'),'Economics','BA'),'Elementary','BA'),'Elementary','EdD'),'Elementary','MS'),'Info Sc','BS'),'Secondary','EdD'),'Secondary','MS');
/*!40000 ALTER TABLE `program` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-16 16:43:50
