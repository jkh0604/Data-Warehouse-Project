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
-- Table structure for table `academics`
--

DROP TABLE IF EXISTS `academics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `academics` (
  `AcademicID` int NOT NULL,
  `GPA` decimal(3,2) DEFAULT NULL,
  `gpaQuality` varchar(6) GENERATED ALWAYS AS ((case when (`GPA` >= 3.0) then _utf8mb4'high' when (`GPA` > 2.0) then _utf8mb4'medium' else _utf8mb4'low' end)) STORED,
  `Status` varchar(1) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`AcademicID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academics`
--

LOCK TABLES `academics` WRITE;
/*!40000 ALTER TABLE `academics` DISABLE KEYS */;
INSERT INTO `academics` (`AcademicID`, `GPA`, `Status`, `Name`, `Address`) VALUES (100,3.10,'I','A. Jones','Little Rock'),(101,3.20,'N','A. Jones','Little Rock'),(107,3.90,'N','M. Kochaal','Savannah'),(108,3.90,'O','M. Big','Little Rock'),(109,4.00,'I','P. Board','Atlanta'),(110,4.00,'O','G. Bear','Little Rock'),(117,3.90,'O','W. Big','Little Rock'),(132,3.90,'N','A. White','Orlando'),(150,3.90,'I','A. Cool','Orlando'),(165,3.30,'O','A. Silver','Seattle'),(175,3.20,'N','K. Glob','Dallas'),(185,4.00,'N','X. Jones','New York'),(195,2.10,'O','D. Red','Seattle'),(199,4.00,'I','K. Duell','Atlanta'),(200,3.20,'I','B. Brady','Little Rock'),(201,3.20,'I','W. Brady','Conway'),(202,3.20,'N','A. Bank','Conway'),(203,3.90,'N','Y. Little','Atlanta'),(205,3.20,'N','K. Minges','Conway'),(207,3.90,'N','K. Goolar','Atlanta'),(208,3.90,'N','P. Little','Atlanta'),(215,3.20,'N','K. King','Conway'),(222,3.90,'N','D. Abul','Savannah'),(229,3.00,'N','M. Katchal','Savannah'),(232,3.10,'I','K. Blue','Little Rock'),(250,3.10,'N','K. Jones','Little Rock'),(255,3.90,'N','K. Dool','Atlanta'),(299,3.00,'N','M. Golab','Seattle'),(300,2.20,'I','C. Cook','Little Rock'),(305,3.20,'N','H. Molar','Conway'),(306,3.20,'N','M. Searsy','Conway'),(307,3.20,'N','M. Korp','Conway'),(308,3.20,'N','M. Kartsoo','Conway'),(315,3.20,'N','M. Gola','Conway'),(329,3.00,'N','G. Kooper','Savannah'),(333,2.90,'N','G. Halk','Atlanta'),(337,2.80,'O','N. Mikhy','Savannah'),(338,3.90,'O','M. Bayraq','Savannah'),(339,3.90,'N','H. Poory','Atlanta'),(350,4.00,'N','C. Cool','Pine Bluff'),(352,3.80,'O','C. Black','Pine Bluff'),(356,4.00,'I','C. Brown','Denver'),(357,4.00,'O','C. Brown','Denver'),(391,3.20,'N','X. Searsy','Conway'),(400,3.90,'N','D. Morty','Atlanta'),(401,3.90,'I','D. Morgan','Conway'),(402,2.10,'I','D. Morty','Seattle'),(407,3.10,'O','T. Doolak','Seattle'),(415,3.20,'N','T. King','Conway'),(416,3.20,'N','T. Gola','Conway'),(417,3.90,'O','T. Dool','Atlanta'),(418,4.00,'O','T. Brown','Denver'),(419,2.10,'O','T. Red','Seattle'),(420,3.30,'N','T. Silver','Seattle'),(421,3.20,'I','T. Chen','Conway'),(422,3.20,'O','U. Yu','Conway'),(423,3.90,'O','U. Mooshe','Atlanta'),(431,4.10,'O','W. Goos','Savannah'),(439,2.80,'O','H. Mishu','Savannah'),(452,3.20,'I','N. Brady','Little Rock'),(473,4.00,'I','M. Browny','Seattle'),(500,3.20,'O','K. Bronz','Dallas'),(524,4.00,'I','U. Alramzy','Denver'),(529,3.20,'I','M. Yu','Conway'),(552,3.90,'O','K. Ahmad','Atlanta'),(579,3.10,'I','U. Jones','Little Rock'),(590,2.20,'N','X. Cook','Little Rock'),(591,3.90,'N','Z. Kochaal','Savannah'),(600,4.00,'O','C. Jones','Dallas'),(609,4.00,'O','N. Gearsal','Little Rock'),(612,4.00,'I','V. Board','Atlanta'),(615,3.20,'N','K. Jiring','Conway'),(650,3.90,'N','D. Sorty','Atlanta'),(653,4.00,'O','C. Alshukri','Denver'),(665,3.30,'I','Z. Silver','Seattle'),(667,3.20,'O','K. Chen','Conway'),(680,3.80,'O','Y. Brady','Pine Bluff'),(681,3.20,'N','Y. Brady','Little Rock'),(682,2.20,'O','Y. Cook','Little Rock'),(687,3.90,'N','Y. Morty','Atlanta'),(688,2.20,'N','Y. Crema','Little Rock'),(689,3.90,'N','Y. Morgan','Conway'),(690,3.90,'N','D. Brown','Atlanta'),(699,3.00,'N','A. Woo','Seattle'),(700,3.30,'I','A. Boss','Seattle'),(702,3.20,'I','Y. Brady','Conway'),(703,3.20,'O','Y. Bank','Conway'),(715,3.20,'N','M. Chendo','Conway'),(739,3.10,'N','A. Moon','Little Rock'),(750,3.20,'N','K. Gold','Dallas'),(800,3.20,'O','K. Queen','Conway'),(839,3.80,'N','Q. Robe','Pine Bluff'),(850,4.00,'I','F. Jones','New York'),(855,3.90,'N','Z. Megart','Atlanta'),(900,3.20,'I','B. Gola','Conway'),(901,2.20,'O','C. Crema','Little Rock'),(939,3.10,'O','U. Wang','Little Rock'),(950,2.10,'I','D. Golden','Seattle'),(955,3.90,'O','K. Booth','Atlanta'),(956,4.00,'O','C. Jessy','Orlando'),(986,3.80,'N','Q. Brady','Pine Bluff');
/*!40000 ALTER TABLE `academics` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-07 17:03:17
