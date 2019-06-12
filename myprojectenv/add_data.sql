-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: sling
-- ------------------------------------------------------
-- Server version	5.7.26

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
-- Table structure for table `borrowers`
--

DROP TABLE IF EXISTS `borrowers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `borrowers` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `loan_size` int(11) DEFAULT NULL,
  `loan_duration` int(11) DEFAULT NULL,
  `interest` int(11) NOT NULL,
  `email` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `borrowers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowers`
--

LOCK TABLES `borrowers` WRITE;
/*!40000 ALTER TABLE `borrowers` DISABLE KEYS */;
INSERT INTO `borrowers` VALUES ('07bc8135-758b-49b6-a480-eaf2cea1e321','2019-06-12 00:21:04',10,5,2,'silver@','c511827a-4277-4a39-850a-660aff104ae4'),('8107fa63-d9fc-4796-858c-447e9f05614a','2019-06-12 00:25:30',50,25,6,'charles@','d0fb9732-c803-40e7-a06e-7713a05ca470'),('b64cb8c1-c356-4b24-89fa-c3aa118a9795','2019-06-12 00:21:54',20,10,2,'phu@','4ae68e58-9ca3-467f-8572-76ec3435443d'),('e29cfdb2-495d-4665-ab57-b379ccdb5ecd','2019-06-12 00:23:08',30,15,4,'samie@','45776582-7929-43cc-9330-1212d9a1d9af'),('ea0392d8-bbbc-478a-96d1-615f7a5c9d11','2019-06-12 00:24:14',40,20,4,'chris@','c391c945-23a4-42e4-91e2-4581adbfe6aa');
/*!40000 ALTER TABLE `borrowers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lenders`
--

DROP TABLE IF EXISTS `lenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lenders` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `loan_size` int(11) DEFAULT NULL,
  `loan_duration` int(11) DEFAULT NULL,
  `interest` int(11) NOT NULL,
  `email` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `lenders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lenders`
--

LOCK TABLES `lenders` WRITE;
/*!40000 ALTER TABLE `lenders` DISABLE KEYS */;
INSERT INTO `lenders` VALUES ('0f9c2669-8ffb-4c3e-8838-c4079aad05dd','2019-06-12 00:29:16',10,5,2,'silver@','c511827a-4277-4a39-850a-660aff104ae4'),('2dadadce-e3a5-48e8-85fb-67cce7248eef','2019-06-12 00:31:29',30,15,4,'samie@','45776582-7929-43cc-9330-1212d9a1d9af'),('7d0b1b00-1e28-4aba-9462-468995f1aa1a','2019-06-12 00:33:28',50,25,6,'charles@','d0fb9732-c803-40e7-a06e-7713a05ca470'),('8c32af7a-0a8f-4c89-98fc-30158128de11','2019-06-12 00:30:43',20,10,2,'phu@','4ae68e58-9ca3-467f-8572-76ec3435443d'),('c9a58e93-6912-49ce-8ba7-6431b0332b8e','2019-06-12 00:32:22',40,20,4,'chris@','c391c945-23a4-42e4-91e2-4581adbfe6aa');
/*!40000 ALTER TABLE `lenders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `amount_borrowed` int(11) DEFAULT NULL,
  `amount_lent` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('45776582-7929-43cc-9330-1212d9a1d9af','2019-06-12 00:15:15','samie@','9ddf6d7e30b59d44ad2a640ee0946638','samie','Azad',30,40),('4ae68e58-9ca3-467f-8572-76ec3435443d','2019-06-12 00:14:02','phu@','9ddf6d7e30b59d44ad2a640ee0946638','phu','truong',20,30),('c391c945-23a4-42e4-91e2-4581adbfe6aa','2019-06-12 00:15:59','chris@','9ddf6d7e30b59d44ad2a640ee0946638','Chris','Choe',40,50),('c511827a-4277-4a39-850a-660aff104ae4','2019-06-12 00:11:38','silver@','9ddf6d7e30b59d44ad2a640ee0946638','stef','silver',10,20),('d0fb9732-c803-40e7-a06e-7713a05ca470','2019-06-12 00:17:31','charles@','9ddf6d7e30b59d44ad2a640ee0946638','Charles','Stewart',5000000,0);
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

-- Dump completed on 2019-06-12  0:35:20
