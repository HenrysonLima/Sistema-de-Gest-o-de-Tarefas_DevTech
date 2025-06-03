-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: devTech_database
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_admin`
--

DROP TABLE IF EXISTS `t_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_admin` (
  `id_admin` int(11) NOT NULL AUTO_INCREMENT,
  `username_admin` varchar(100) NOT NULL,
  `password_admin` varchar(100) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_admin`
--

LOCK TABLES `t_admin` WRITE;
/*!40000 ALTER TABLE `t_admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_grupo`
--

DROP TABLE IF EXISTS `t_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_grupo` (
  `id_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `turno` varchar(100) NOT NULL,
  `id_tarefa` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_grupo`),
  KEY `t_grupo_t_tarefa_FK` (`id_tarefa`),
  CONSTRAINT `t_grupo_t_tarefa_FK` FOREIGN KEY (`id_tarefa`) REFERENCES `t_tarefa` (`id_tarefa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_grupo`
--

LOCK TABLES `t_grupo` WRITE;
/*!40000 ALTER TABLE `t_grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_rel_utilizador_grupo`
--

DROP TABLE IF EXISTS `t_rel_utilizador_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_rel_utilizador_grupo` (
  `id_rel_utilizador_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `id_utilizador` int(11) DEFAULT NULL,
  `id_grupo` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_rel_utilizador_grupo`),
  KEY `t_rel_utilizador_grupo_t_utilizador_FK` (`id_utilizador`),
  KEY `t_rel_utilizador_grupo_t_grupo_FK` (`id_grupo`),
  CONSTRAINT `t_rel_utilizador_grupo_t_grupo_FK` FOREIGN KEY (`id_grupo`) REFERENCES `t_grupo` (`id_grupo`),
  CONSTRAINT `t_rel_utilizador_grupo_t_utilizador_FK` FOREIGN KEY (`id_utilizador`) REFERENCES `t_utilizador` (`id_utilizador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_rel_utilizador_grupo`
--

LOCK TABLES `t_rel_utilizador_grupo` WRITE;
/*!40000 ALTER TABLE `t_rel_utilizador_grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_rel_utilizador_grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_tarefa`
--

DROP TABLE IF EXISTS `t_tarefa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_tarefa` (
  `id_tarefa` int(11) NOT NULL AUTO_INCREMENT,
  `descricao_tarefa` varchar(100) NOT NULL,
  `estado_tarefa` varchar(100) NOT NULL,
  `data_inicio` date DEFAULT NULL,
  `data_conclusao` date DEFAULT NULL,
  PRIMARY KEY (`id_tarefa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_tarefa`
--

LOCK TABLES `t_tarefa` WRITE;
/*!40000 ALTER TABLE `t_tarefa` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_tarefa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_utilizador`
--

DROP TABLE IF EXISTS `t_utilizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_utilizador` (
  `id_utilizador` int(11) NOT NULL AUTO_INCREMENT,
  `username_utilizador` varchar(100) NOT NULL,
  `password_utilizador` varchar(100) NOT NULL,
  PRIMARY KEY (`id_utilizador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_utilizador`
--

LOCK TABLES `t_utilizador` WRITE;
/*!40000 ALTER TABLE `t_utilizador` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_utilizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'devTech_database'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-03 19:24:54
