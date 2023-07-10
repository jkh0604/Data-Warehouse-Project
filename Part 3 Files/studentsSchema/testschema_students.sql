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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `AcademicID` int NOT NULL,
  `CollegeID` varchar(5) NOT NULL,
  `SemesterID` varchar(4) NOT NULL,
  PRIMARY KEY (`AcademicID`,`CollegeID`,`SemesterID`),
  KEY `CollegeID` (`CollegeID`),
  KEY `SemesterID` (`SemesterID`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`AcademicID`) REFERENCES `academics` (`AcademicID`),
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`CollegeID`) REFERENCES `program` (`CollegeID`),
  CONSTRAINT `students_ibfk_3` FOREIGN KEY (`SemesterID`) REFERENCES `time` (`SemesterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (850,'InBS','FA85'),(950,'InBS','FA85'),(109,'ChAS','FA88'),(110,'BiAS','FA88'),(199,'BiAS','FA88'),(402,'InBS','FA88'),(600,'InBS','FA88'),(609,'BiBS','FA88'),(612,'ChAS','FA88'),(356,'ApPhD','FA89'),(357,'ApPhD','FA89'),(956,'ApMS','FA89'),(185,'InBS','FA90'),(195,'InBS','FA90'),(653,'ApPhD','FA91'),(418,'ApPhD','FA92'),(419,'InBS','FA92'),(524,'ApPhD','FA92'),(739,'CoBS','S184'),(300,'BiBS','S187'),(682,'BiBS','S187'),(688,'BiAS','S187'),(901,'BiAS','S187'),(407,'B MBA','S192'),(590,'BiAS','S192'),(305,'BiMS','S284'),(306,'BiMS','S284'),(307,'BiMS','S284'),(308,'BiMS','S284'),(391,'BiMS','S284'),(400,'BiBS','S284'),(650,'BiBS','S284'),(687,'CoBS','S284'),(750,'ApPhD','S284'),(203,'ChMS','S286'),(207,'ChMS','S286'),(208,'ChMS','S286'),(255,'SeMS','S286'),(855,'SeMS','S286'),(202,'ApPhD','S287'),(401,'BiBS','S287'),(552,'SeEdD','S287'),(689,'BiBS','S287'),(500,'ChMS','S288'),(690,'BiBS','S288'),(175,'ApPhD','S289'),(423,'SeEdD','S290'),(417,'SeMS','S292'),(703,'ApPhD','S387'),(205,'ElEdD','S484'),(215,'ElEdD','S484'),(700,'ElMS','S484'),(165,'ElMS','S485'),(150,'CoMS','S486'),(250,'CoBS','S486'),(350,'ApMS','S486'),(337,'B BA','S487'),(338,'B MBA','S487'),(339,'B BA','S487'),(439,'AcBA','S487'),(452,'ApPhD','S488'),(800,'ElEdD','S489'),(222,'EcBA','S490'),(333,'B MBA','S490'),(352,'ApPhD','S490'),(415,'ElEdD','S490'),(431,'AcBA','S490'),(229,'EcBA','S491'),(232,'CoAS','S491'),(329,'AcBA','S491'),(420,'ElEdD','S491'),(421,'ElEdD','S491'),(665,'ElEdD','S491'),(132,'CoAS','S492'),(667,'ElEdD','S492'),(100,'CoBS','SP84'),(299,'ChBS','SP84'),(315,'SeMS','SP84'),(579,'CoBS','SP84'),(715,'SeMS','SP84'),(101,'CoMS','SP87'),(201,'ApPhD','SP87'),(702,'ApPhD','SP87'),(900,'SeMS','SP87'),(955,'SeMS','SP87'),(986,'CoMS','SP87'),(422,'SeMS','SP90'),(529,'SeMS','SP90'),(680,'CoMS','SP90'),(681,'ApPhD','SP91'),(107,'ChBS','SP92'),(108,'ChBS','SP92'),(117,'ChBS','SP92'),(200,'ApPhD','SP92'),(473,'CoPhD','SP92'),(591,'ChBS','SP92'),(699,'ElBA','SP92');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
