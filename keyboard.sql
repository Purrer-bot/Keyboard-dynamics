CREATE DATABASE  IF NOT EXISTS `keyboard` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `keyboard`;
-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: keyboard
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `phrases`
--

DROP TABLE IF EXISTS `phrases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phrases` (
  `phrase_text` varchar(50) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phrases`
--

LOCK TABLES `phrases` WRITE;
/*!40000 ALTER TABLE `phrases` DISABLE KEYS */;
INSERT INTO `phrases` VALUES ('***Тштт** уои.*йпкп**ыы с***тй ***лнк***псо***еие',1),('***Лса***н п.** а м**тзло***уер***еид***знн***еал',2),('е**Впо **т вйд*чоии.* нжщт**о яе**,вра**ттол**оит',3),('ч**Моки**рбилн*оатби*п о м.*нкиа** м к**реии**ища',4),('ш**Пнхл**й ыоь*у,дб**л то***ооп***ат .**ждье**оаа',5),('т**Эрсм**дпасо*о ж .*коуее**т нт** н и**ос,р**тое',6),('р**Еооп.*ипл е* сгенеяу ыны*зюне** аьм**еьле**щлб',7),('тт*Олк а*иеаоч*ттрндлаеп ое*ы ,п**рии .*внкоь*тьт',8),('***Пд ы** оем.*йким**олха***пор***хрг***о о***л,п',9),('ыдЭннооеан чрмт т еосй.ть',10);
/*!40000 ALTER TABLE `phrases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `passphrase` int(11) DEFAULT NULL,
  `ideal_value` double DEFAULT NULL,
  `difference` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `passphrase` (`passphrase`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`passphrase`) REFERENCES `phrases` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Pusheen',1,0.20000000298023224,1.34564e-17),(2,'ЗХщц',1,0.2,-8.95082e-18),(3,'Push',1,0.2,0.004),(4,'Pow',2,0.23034297638252,1.31733e-17),(5,'Skitty',10,0.298153117659014,3.35533e-18),(6,'Ш.Табунщика',3,0.258609526117819,-2.89074e-18),(7,'s-k',1,0.388462253151181,-3.10176e-18);
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

-- Dump completed on 2019-05-18 23:01:56
