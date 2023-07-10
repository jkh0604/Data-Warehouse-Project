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
-- Table structure for table `staging`
--

DROP TABLE IF EXISTS `staging`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staging` (
  `ID` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Major` varchar(45) DEFAULT NULL,
  `Degree` varchar(45) DEFAULT NULL,
  `GPA` decimal(3,2) DEFAULT NULL,
  `MonthDay` varchar(45) DEFAULT NULL,
  `Y` int DEFAULT NULL,
  `Status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staging`
--

LOCK TABLES `staging` WRITE;
/*!40000 ALTER TABLE `staging` DISABLE KEYS */;
INSERT INTO `staging` VALUES (100,'A. Jones','Little Rock','Computer Sc','BS',3.10,'May-15',84,'I'),(101,'A. Jones','Little Rock','Computer Sc','MS',3.20,'May-15',87,'N'),(107,'M. Kochaal','Savannah','Chemistry','BS',3.90,'May-15',92,'N'),(108,'M. Big','Little Rock','Chemistry','BS',3.90,'May-15',92,'O'),(109,'P. Board','Atlanta','Chemistry','AS',4.00,'Dec-15',88,'I'),(110,'G. Bear','Little Rock','Biology','AS',4.00,'Dec-15',88,'O'),(117,'W. Big','Little Rock','Chemistry','BS',3.90,'May-15',92,'O'),(132,'A. White','Orlando','Computer Sc','AS',3.90,'Aug-15',92,'N'),(150,'A. Cool','Orlando','Computer Sc','MS',3.90,'Aug-15',86,'I'),(165,'A. Silver','Seattle','Elementary','MS',3.30,'Aug-15',85,'O'),(175,'K. Glob','Dallas','Applied Sc','PhD',3.20,'Jul-4',89,'N'),(185,'X. Jones','New York','Info Sc','BS',4.00,'Dec-15',90,'N'),(195,'D. Red','Seattle','Info Sc','BS',2.10,'Dec-15',90,'O'),(199,'K. Duell','Atlanta','Biology','AS',4.00,'Dec-15',88,'I'),(200,'B. Brady','Little Rock','Applied Sc','PhD',3.20,'May-15',92,'I'),(201,'W. Brady','Conway','Applied Sc','PhD',3.20,'May-15',87,'I'),(202,'A. Bank','Conway','Applied Sc','PhD',3.20,'Jul-4',87,'N'),(203,'Y. Little','Atlanta','Chemistry','MS',3.90,'Jul-4',86,'N'),(205,'K. Minges','Conway','Elementary','EdD',3.20,'Aug-15',84,'N'),(207,'K. Goolar','Atlanta','Chemistry','MS',3.90,'Jul-4',86,'N'),(208,'P. Little','Atlanta','Chemistry','MS',3.90,'Jul-4',86,'N'),(215,'K. King','Conway','Elementary','EdD',3.20,'Aug-15',84,'N'),(222,'D. Abul','Savannah','Economics','BA',3.90,'Aug-15',90,'N'),(229,'M. Katchal','Savannah','Economics','BA',3.00,'Aug-15',91,'N'),(232,'K. Blue','Little Rock','Computer Sc','AS',3.10,'Aug-15',91,'I'),(250,'K. Jones','Little Rock','Computer Sc','BS',3.10,'Aug-15',86,'N'),(255,'K. Dool','Atlanta','Secondary','MS',3.90,'Jul-4',86,'N'),(299,'M. Golab','Seattle','Chemistry','BS',3.00,'May-15',84,'N'),(300,'C. Cook','Little Rock','Biology','BS',2.20,'Jun-1',87,'I'),(305,'H. Molar','Conway','Biology','MS',3.20,'Jul-4',84,'N'),(306,'M. Searsy','Conway','Biology','MS',3.20,'Jul-4',84,'N'),(307,'M. Korp','Conway','Biology','MS',3.20,'Jul-4',84,'N'),(308,'M. Kartsoo','Conway','Biology','MS',3.20,'Jul-4',84,'N'),(315,'M. Gola','Conway','Secondary','MS',3.20,'May-15',84,'N'),(329,'G. Kooper','Savannah','Accounting','BA',3.00,'Aug-15',91,'N'),(333,'G. Halk','Atlanta','B Admin','MBA',2.90,'Aug-15',90,'N'),(337,'N. Mikhy','Savannah','B Admin','BA',2.80,'Aug-15',87,'O'),(338,'M. Bayraq','Savannah','B Admin','MBA',3.90,'Aug-15',87,'O'),(339,'H. Poory','Atlanta','B Admin','BA',3.90,'Aug-15',87,'N'),(350,'C. Cool','Pine Bluff','Applied Sc','MS',4.00,'Aug-15',86,'N'),(352,'C. Black','Pine Bluff','Applied Sc','PhD',3.80,'Aug-15',90,'O'),(356,'C. Brown','Denver','Applied Sc','PhD',4.00,'Dec-15',89,'I'),(357,'C. Brown','Denver','Applied Sc','PhD',4.00,'Dec-15',89,'O'),(391,'X. Searsy','Conway','Biology','MS',3.20,'Jul-4',84,'N'),(400,'D. Morty','Atlanta','Biology','BS',3.90,'Jul-4',84,'N'),(401,'D. Morgan','Conway','Biology','BS',3.90,'Jul-4',87,'I'),(402,'D. Morty','Seattle','Info Sc','BS',2.10,'Dec-15',88,'I'),(407,'T. Doolak','Seattle','B Admin','MBA',3.10,'Jun-1',92,'O'),(415,'T. King','Conway','Elementary','EdD',3.20,'Aug-15',90,'N'),(416,'T. Gola','Conway','Seconday','MS',3.20,'May-15',90,'N'),(417,'T. Dool','Atlanta','Secondary','MS',3.90,'Jul-4',92,'O'),(418,'T. Brown','Denver','Applied Sc','PhD',4.00,'Dec-15',92,'O'),(419,'T. Red','Seattle','Info Sc','BS',2.10,'Dec-15',92,'O'),(420,'T. Silver','Seattle','Elementary','EdD',3.30,'Aug-15',91,'N'),(421,'T. Chen','Conway','Elementary','EdD',3.20,'Aug-15',91,'I'),(422,'U. Yu','Conway','Secondary','MS',3.20,'May-15',90,'O'),(423,'U. Mooshe','Atlanta','Secondary','EdD',3.90,'Jul-4',90,'O'),(431,'W. Goos','Savannah','Accounting','BA',4.10,'Aug-15',90,'O'),(439,'H. Mishu','Savannah','Accounting','BA',2.80,'Aug-15',87,'O'),(452,'N. Brady','Little Rock','Applied Sc','PhD',3.20,'Aug-15',88,'I'),(473,'M. Browny','Seattle','Computer Sc','PhD',4.00,'May-15',92,'I'),(500,'K. Bronz','Dallas','Chemistry','MS',3.20,'Jul-4',88,'O'),(524,'U. Alramzy','Denver','Applied Sc','PhD',4.00,'Dec-15',92,'I'),(529,'M. Yu','Conway','Secondary','MS',3.20,'May-15',90,'I'),(552,'K. Ahmad','Atlanta','Secondary','EdD',3.90,'Jul-4',87,'O'),(579,'U. Jones','Little Rock','Computer Sc','BS',3.10,'May-15',84,'I'),(590,'X. Cook','Little Rock','Biology','AS',2.20,'Jun-1',92,'N'),(591,'Z. Kochaal','Savannah','Chemistry','BS',3.90,'May-15',92,'N'),(600,'C. Jones','Dallas','Info Sc','BS',4.00,'Dec-15',88,'O'),(609,'N. Gearsal','Little Rock','Biology','BS',4.00,'Dec-15',88,'O'),(612,'V. Board','Atlanta','Chemistry','AS',4.00,'Dec-15',88,'I'),(615,'K. Jiring','Conway','Element','BA',3.20,'Aug-15',84,'N'),(650,'D. Sorty','Atlanta','Biology','BS',3.90,'Jul-4',84,'N'),(653,'C. Alshukri','Denver','Applied Sc','PhD',4.00,'Dec-15',91,'O'),(665,'Z. Silver','Seattle','Elementary','EdD',3.30,'Aug-15',91,'I'),(667,'K. Chen','Conway','Elementary','EdD',3.20,'Aug-15',92,'O'),(680,'Y. Brady','Pine Bluff','Computer Sc','MS',3.80,'May-15',90,'O'),(681,'Y. Brady','Little Rock','Applied Sc','PhD',3.20,'May-15',91,'N'),(682,'Y. Cook','Little Rock','Biology','BS',2.20,'Jun-1',87,'O'),(687,'Y. Morty','Atlanta','Computer Sc','BS',3.90,'Jul-4',84,'N'),(688,'Y. Crema','Little Rock','Biology','AS',2.20,'Jun-1',87,'N'),(689,'Y. Morgan','Conway','Biology','BS',3.90,'Jul-4',87,'N'),(690,'D. Brown','Atlanta','Biology','BS',3.90,'Jul-4',88,'N'),(699,'A. Woo','Seattle','Elementary','BA',3.00,'May-15',92,'N'),(700,'A. Boss','Seattle','Elementary','MS',3.30,'Aug-15',84,'I'),(702,'Y. Brady','Conway','Applied Sc','PhD',3.20,'May-15',87,'I'),(703,'Y. Bank','Conway','Applied Sc','PhD',3.20,'Jul-15',87,'O'),(715,'M. Chendo','Conway','Secondary','MS',3.20,'May-15',84,'N'),(739,'A. Moon','Little Rock','Computer Sc','BS',3.10,'Jun-1',84,'N'),(750,'K. Gold','Dallas','Applied Sc','PhD',3.20,'Jul-4',84,'N'),(800,'K. Queen','Conway','Elementary','EdD',3.20,'Aug-15',89,'O'),(839,'Q. Robe','Pine Bluff','Computer Sc','MS',3.80,'Jun-18',87,'N'),(850,'F. Jones','New York','Info Sc','BS',4.00,'Dec-15',85,'I'),(855,'Z. Megart','Atlanta','Secondary','MS',3.90,'Jul-4',86,'N'),(900,'B. Gola','Conway','Secondary','MS',3.20,'May-15',87,'I'),(901,'C. Crema','Little Rock','Biology','AS',2.20,'Jun-1',87,'O'),(939,'U. Wang','Little Rock','Computer Sc','AS',3.10,'Jul-15',84,'O'),(950,'D. Golden','Seattle','Info Sc','BS',2.10,'Dec-15',85,'I'),(955,'K. Booth','Atlanta','Secondary','MS',3.90,'May-15',87,'O'),(956,'C. Jessy','Orlando','Applied Sc','MS',4.00,'Dec-15',89,'O'),(986,'Q. Brady','Pine Bluff','Computer Sc','MS',3.80,'May-15',87,'N');
/*!40000 ALTER TABLE `staging` ENABLE KEYS */;
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
