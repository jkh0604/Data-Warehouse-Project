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
-- Table structure for table `time`
--

DROP TABLE IF EXISTS `time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `time` (
  `SemesterID` varchar(4) GENERATED ALWAYS AS ((case when ((left(`MonthDay`,3) = _utf8mb4'Jul') and (right(`MonthDay`,1) = _utf8mb4'4')) then concat(_utf8mb4'S2',_utf8mb4'',`Y`) when ((left(`MonthDay`,3) = _utf8mb4'Jul') and (right(`MonthDay`,1) = _utf8mb4'5')) then concat(_utf8mb4'S3',_utf8mb4'',`Y`) when (left(`MonthDay`,3) = _utf8mb4'Jun') then concat(_utf8mb4'S1',_utf8mb4'',`Y`) when (left(`MonthDay`,1) = _utf8mb4'A') then concat(_utf8mb4'S4',_utf8mb4'',`Y`) when (left(`MonthDay`,1) = _utf8mb4'D') then concat(_utf8mb4'FA',_utf8mb4'',`Y`) when (left(`MonthDay`,1) = _utf8mb4'M') then concat(_utf8mb4'SP',_utf8mb4'',`Y`) else _utf8mb4'NA' end)) STORED NOT NULL,
  `MonthDay` varchar(45) DEFAULT NULL,
  `Y` int DEFAULT NULL,
  PRIMARY KEY (`SemesterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `time`
--

LOCK TABLES `time` WRITE;
/*!40000 ALTER TABLE `time` DISABLE KEYS */;
INSERT INTO `time` (`MonthDay`, `Y`) VALUES ,'Dec-15',85),,'Dec-15',85),'Dec-15',88),,'Dec-15',85),'Dec-15',88),'Dec-15',89),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),'May-15',84),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),'May-15',84),'May-15',87),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),'May-15',84),'May-15',87),'May-15',90),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),'May-15',84),'May-15',87),'May-15',90),'May-15',91),,'Dec-15',85),'Dec-15',88),'Dec-15',89),'Dec-15',90),'Dec-15',91),'Dec-15',92),'Jun-1',84),'Jun-1',87),'Jun-1',92),'Jul-4',84),'Jul-4',86),'Jul-4',87),'Jul-4',88),'Jul-4',89),'Jul-4',90),'Jul-4',92),'Jul-15',87),'Aug-15',84),'Aug-15',85),'Aug-15',86),'Aug-15',87),'Aug-15',88),'Aug-15',89),'Aug-15',90),'Aug-15',91),'Aug-15',92),'May-15',84),'May-15',87),'May-15',90),'May-15',91),'May-15',92);
/*!40000 ALTER TABLE `time` ENABLE KEYS */;
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
