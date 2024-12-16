-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: preserved
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `class_code` varchar(10) NOT NULL,
  `class_description` varchar(255) NOT NULL,
  PRIMARY KEY (`class_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES ('A1','Express Passenger'),('A2','Heavy Freight'),('A3','Mixed Traffic'),('B1','Shunting Engine'),('B2','Industrial Locomotive'),('C1','Specialized Locomotive'),('C2','Preserved Historic'),('C3','Tourist Engine'),('D1','Diesel-Electric'),('D2','Steam-Diesel Hybrid'),('E1','Electric Locomotive'),('E2','High-Speed Rail'),('E3','Urban Transit'),('F1','Light Rail'),('F2','Maglev'),('F3','Prototype'),('G1','Articulated Engine'),('G2','Tank Engine'),('G3','Switching Locomotive'),('H1','Mountain Climber'),('H2','Snowplow Locomotive'),('H3','Work Train'),('I1','Test Locomotive'),('I2','Military Train'),('I3','Heritage Train');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `origins`
--

DROP TABLE IF EXISTS `origins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `origins` (
  `origin_code` varchar(10) NOT NULL,
  `origin_description` varchar(255) NOT NULL,
  PRIMARY KEY (`origin_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `origins`
--

LOCK TABLES `origins` WRITE;
/*!40000 ALTER TABLE `origins` DISABLE KEYS */;
INSERT INTO `origins` VALUES ('BR','British Railways'),('CR','Caledonian Railway'),('EOR','Epping Ongar Railway'),('ER','Eastern Region'),('GER','Great Eastern Railway'),('GNR','Great Northern Railway'),('GWR','Great Western Railway'),('KWVR','Keighley and Worth Valley Railway'),('LMR','London Midland Region'),('LNER','London North Eastern Railway'),('LNWR','London and North Western Railway'),('LSWR','London and South Western Railway'),('MR','Midland Railway'),('NBR','North British Railway'),('NER','North Eastern Railway'),('NYMR','North Yorkshire Moors Railway'),('SCR','Scottish Central Railway'),('SECR','South Eastern and Chatham Railway'),('SR','Southern Railway'),('SVR','Severn Valley Railway'),('TFL','Transport for London'),('WLLR','Welshpool and Llanfair Light Railway'),('WR','Western Region'),('WSR','West Somerset Railway');
/*!40000 ALTER TABLE `origins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `railway_lines`
--

DROP TABLE IF EXISTS `railway_lines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `railway_lines` (
  `line_number` int NOT NULL AUTO_INCREMENT,
  `class_code` varchar(10) DEFAULT NULL,
  `origin_code` varchar(10) DEFAULT NULL,
  `type_code` varchar(10) DEFAULT NULL,
  `steam_or_diesel` varchar(50) DEFAULT NULL,
  `line_name` varchar(255) DEFAULT NULL,
  `address` text,
  `phone_number` varchar(15) DEFAULT NULL,
  `fax_number` varchar(15) DEFAULT NULL,
  `nearest_mainline_station` varchar(255) DEFAULT NULL,
  `resident_locos_url` text,
  `route_map_url` text,
  `website_url` text,
  `total_miles` decimal(5,2) DEFAULT NULL,
  `year_opened` int DEFAULT NULL,
  `membership_prices` decimal(10,2) DEFAULT NULL,
  `year_built` int DEFAULT NULL,
  `other_details` text,
  PRIMARY KEY (`line_number`),
  KEY `class_code` (`class_code`),
  KEY `origin_code` (`origin_code`),
  KEY `type_code` (`type_code`),
  CONSTRAINT `railway_lines_ibfk_1` FOREIGN KEY (`class_code`) REFERENCES `classes` (`class_code`),
  CONSTRAINT `railway_lines_ibfk_2` FOREIGN KEY (`origin_code`) REFERENCES `origins` (`origin_code`),
  CONSTRAINT `railway_lines_ibfk_3` FOREIGN KEY (`type_code`) REFERENCES `types` (`type_code`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `railway_lines`
--

LOCK TABLES `railway_lines` WRITE;
/*!40000 ALTER TABLE `railway_lines` DISABLE KEYS */;
INSERT INTO `railway_lines` VALUES (1,'A1','LNER','4-6-2','Steam','Flying Scotsman Line','123 Railway St, York, UK','01904 123456','01904 654321','York Station','http://locos.lner.com','http://maps.lner.com','http://lner.com',12.50,1863,50.00,1923,'Famous line'),(2,'B1','GWR','2-8-0','Diesel','Western Freight Line','456 Western Ave, Swindon, UK','01793 123456','01793 654321','Swindon Station','http://locos.gwr.com','http://maps.gwr.com','http://gwr.com',22.70,1851,60.00,1930,'Known for freight'),(3,'C2','SR','4-4-2','Steam','Southern Belle Line','789 Southern St, Brighton, UK','01273 123456','01273 654321','Brighton Station','http://locos.sr.com','http://maps.sr.com','http://sr.com',15.30,1877,45.00,1925,'Tourist favorite'),(4,'D1','BR','0-6-0','Diesel','British Mainline','101 BR St, London, UK','020 12345678','020 87654321','London Victoria','http://locos.br.com','http://maps.br.com','http://br.com',45.00,1948,80.00,1950,'Major route');
/*!40000 ALTER TABLE `railway_lines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `station_stops`
--

DROP TABLE IF EXISTS `station_stops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station_stops` (
  `station_id` int NOT NULL AUTO_INCREMENT,
  `line_id` int DEFAULT NULL,
  `next_station_id` int DEFAULT NULL,
  `station_name` varchar(255) DEFAULT NULL,
  `first_stop_yn` tinyint(1) DEFAULT NULL,
  `last_stop_yn` tinyint(1) DEFAULT NULL,
  `other_details` text,
  PRIMARY KEY (`station_id`),
  KEY `line_id` (`line_id`),
  KEY `next_station_id` (`next_station_id`),
  CONSTRAINT `station_stops_ibfk_1` FOREIGN KEY (`line_id`) REFERENCES `railway_lines` (`line_number`),
  CONSTRAINT `station_stops_ibfk_2` FOREIGN KEY (`next_station_id`) REFERENCES `station_stops` (`station_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station_stops`
--

LOCK TABLES `station_stops` WRITE;
/*!40000 ALTER TABLE `station_stops` DISABLE KEYS */;
INSERT INTO `station_stops` VALUES (3,1,NULL,'Edinburgh',0,1,'Scenic destination'),(5,2,NULL,'Bristol',0,1,'Major city'),(7,3,NULL,'Eastbourne',0,1,'Tourist favorite'),(9,4,NULL,'Gatwick Airport',0,1,'International connection');
/*!40000 ALTER TABLE `station_stops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `types` (
  `type_code` varchar(10) NOT NULL,
  `type_description` varchar(255) NOT NULL,
  PRIMARY KEY (`type_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
INSERT INTO `types` VALUES ('0-10-0','Decapod'),('0-4-0','Industrial Switcher'),('0-6-0','Switcher'),('0-8-0','Heavy Switcher'),('2-10-2','Santa Fe Type'),('2-4-0','Single Driver'),('2-6-0','Mogul'),('2-6-2','Prairie Type'),('2-6-6-6','Allegheny'),('2-8-0','Consolidation'),('2-8-2','Mikado'),('2-8-8-2','Mallet Articulated'),('4-10-2','Southern Pacific'),('4-4-0','American Standard'),('4-4-2','Atlantic Type'),('4-6-0','Ten-Wheeler'),('4-6-2','Pacific Type'),('4-6-4','Hudson Type'),('4-8-2','Mountain Type'),('4-8-4','Northern Type');
/*!40000 ALTER TABLE `types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'jhonny','test','admin'),(2,'Anx','root','admin'),(3,'ask','root','admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-16 16:15:39
