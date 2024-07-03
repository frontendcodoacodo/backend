-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: turismo_db2
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `actividad`
--

DROP TABLE IF EXISTS `actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividad`
--

LOCK TABLES `actividad` WRITE;
/*!40000 ALTER TABLE `actividad` DISABLE KEYS */;
INSERT INTO `actividad` VALUES (1,'caminata'),(2,'pesca'),(3,'paseo en bicicleta'),(4,'aerosilla');
/*!40000 ALTER TABLE `actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guia`
--

DROP TABLE IF EXISTS `guia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `dni` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guia`
--

LOCK TABLES `guia` WRITE;
/*!40000 ALTER TABLE `guia` DISABLE KEYS */;
INSERT INTO `guia` VALUES (1,'Juan','11111111'),(2,'Emilce','22222222'),(3,'Agustin','33333333'),(4,'Paula','44444444');
/*!40000 ALTER TABLE `guia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guia_turistica`
--

DROP TABLE IF EXISTS `guia_turistica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guia_turistica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lugar_turistico_id` int(11) NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `guia_id` int(11) NOT NULL,
  `cupo` int(10) unsigned DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `lugar_turistico_id` (`lugar_turistico_id`),
  KEY `guia_id` (`guia_id`),
  CONSTRAINT `guia_turistica_ibfk_1` FOREIGN KEY (`lugar_turistico_id`) REFERENCES `lugar_turistico` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `guia_turistica_ibfk_2` FOREIGN KEY (`guia_id`) REFERENCES `guia` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guia_turistica`
--

LOCK TABLES `guia_turistica` WRITE;
/*!40000 ALTER TABLE `guia_turistica` DISABLE KEYS */;
INSERT INTO `guia_turistica` VALUES (7,1,'2024-01-10','2024-01-20',1,10),(8,2,'2024-09-20','2024-09-30',2,15),(9,3,'2024-04-10','2024-04-20',3,20),(10,4,'2024-11-05','2024-11-15',4,10),(11,1,'2024-02-10','2024-02-20',1,6),(12,2,'2024-08-10','2024-08-20',2,10);
/*!40000 ALTER TABLE `guia_turistica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_turistico`
--

DROP TABLE IF EXISTS `lugar_turistico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lugar_turistico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `actividad_id` int(11) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `actividad_id` (`actividad_id`),
  CONSTRAINT `lugar_turistico_ibfk_1` FOREIGN KEY (`actividad_id`) REFERENCES `actividad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_turistico`
--

LOCK TABLES `lugar_turistico` WRITE;
/*!40000 ALTER TABLE `lugar_turistico` DISABLE KEYS */;
INSERT INTO `lugar_turistico` VALUES (1,'Esteros del Ibera',2,'Antiguos cauces del Rio Paraná forman compleja red de humedales, esteros y lagunas'),(2,'Dique el Cadillal',4,'Cuenta con atractivos naturales que se pueden disfrutar mediante deportes, gastronomia, paseos historicos'),(3,'Jardin de los Poetas',1,'Lugar emblematico y paseo obligado para los que lo caminan'),(4,'Plaza Independencia',3,'Inaugurada en 1863. Ubicada en el centro de la ciudad');
/*!40000 ALTER TABLE `lugar_turistico` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-03 10:37:06
