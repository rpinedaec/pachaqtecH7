CREATE DATABASE  IF NOT EXISTS `PerezdeCuellar-H7` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `PerezdeCuellar-H7`;
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: PerezdeCuellar-H7
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

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
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `idalumnos` int(11) NOT NULL AUTO_INCREMENT,
  `nombrealumno` varchar(45) NOT NULL,
  `apellidoalumno` varchar(45) NOT NULL,
  `correoalumno` varchar(45) NOT NULL,
  `nacalumno` datetime NOT NULL,
  PRIMARY KEY (`idalumnos`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES (1,'Ricardo','avellaneda','mail@mail.com','1985-01-01 00:00:00'),(2,'alberto','soez','mailo@mail.com','1995-02-03 00:00:00');
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `idcursos` int(11) NOT NULL AUTO_INCREMENT,
  `nombrecurso` varchar(45) NOT NULL,
  PRIMARY KEY (`idcursos`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'back-end'),(2,'front-end');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos_has_matricula`
--

DROP TABLE IF EXISTS `cursos_has_matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos_has_matricula` (
  `cursos_idcursos` int(11) NOT NULL,
  `matricula_idmatricula` int(11) NOT NULL,
  PRIMARY KEY (`cursos_idcursos`,`matricula_idmatricula`),
  KEY `fk_cursos_has_matricula_matricula1_idx` (`matricula_idmatricula`),
  KEY `fk_cursos_has_matricula_cursos1_idx` (`cursos_idcursos`),
  CONSTRAINT `fk_cursos_has_matricula_cursos1` FOREIGN KEY (`cursos_idcursos`) REFERENCES `cursos` (`idcursos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_cursos_has_matricula_matricula1` FOREIGN KEY (`matricula_idmatricula`) REFERENCES `matricula` (`idmatricula`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos_has_matricula`
--

LOCK TABLES `cursos_has_matricula` WRITE;
/*!40000 ALTER TABLE `cursos_has_matricula` DISABLE KEYS */;
INSERT INTO `cursos_has_matricula` VALUES (1,1),(2,1),(1,2),(2,2);
/*!40000 ALTER TABLE `cursos_has_matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docentes`
--

DROP TABLE IF EXISTS `docentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `docentes` (
  `iddocentes` int(11) NOT NULL AUTO_INCREMENT,
  `nombredocente` varchar(45) NOT NULL,
  `dnidocente` varchar(45) NOT NULL,
  `correodocente` varchar(45) NOT NULL,
  `nacdocente` datetime NOT NULL,
  PRIMARY KEY (`iddocentes`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docentes`
--

LOCK TABLES `docentes` WRITE;
/*!40000 ALTER TABLE `docentes` DISABLE KEYS */;
INSERT INTO `docentes` VALUES (1,'Roberto Pineda','87542121','profe@mail.com','1983-08-28 00:00:00'),(2,'David Lopez','98653254','mail@mail.com','1983-08-08 00:00:00');
/*!40000 ALTER TABLE `docentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docentes_has_cursos`
--

DROP TABLE IF EXISTS `docentes_has_cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `docentes_has_cursos` (
  `docentes_iddocentes` int(11) NOT NULL,
  `cursos_idcursos` int(11) NOT NULL,
  `salones_idsalones` int(11) NOT NULL,
  `nota` int(11) NOT NULL,
  PRIMARY KEY (`docentes_iddocentes`,`cursos_idcursos`),
  KEY `fk_docentes_has_cursos_cursos1_idx` (`cursos_idcursos`),
  KEY `fk_docentes_has_cursos_docentes1_idx` (`docentes_iddocentes`),
  KEY `fk_docentes_has_cursos_salones1_idx` (`salones_idsalones`),
  CONSTRAINT `fk_docentes_has_cursos_cursos1` FOREIGN KEY (`cursos_idcursos`) REFERENCES `cursos` (`idcursos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_docentes_has_cursos_docentes1` FOREIGN KEY (`docentes_iddocentes`) REFERENCES `docentes` (`iddocentes`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_docentes_has_cursos_salones1` FOREIGN KEY (`salones_idsalones`) REFERENCES `salones` (`idsalones`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docentes_has_cursos`
--

LOCK TABLES `docentes_has_cursos` WRITE;
/*!40000 ALTER TABLE `docentes_has_cursos` DISABLE KEYS */;
INSERT INTO `docentes_has_cursos` VALUES (1,1,1,0),(2,1,2,0);
/*!40000 ALTER TABLE `docentes_has_cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matricula`
--

DROP TABLE IF EXISTS `matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matricula` (
  `idmatricula` int(11) NOT NULL AUTO_INCREMENT,
  `alumnos_idalumnos` int(11) NOT NULL,
  `periodoEscolar_idperiodoEscolar` int(11) NOT NULL,
  PRIMARY KEY (`idmatricula`),
  KEY `fk_matricula_alumnos1_idx` (`alumnos_idalumnos`),
  KEY `fk_matricula_periodoEscolar1_idx` (`periodoEscolar_idperiodoEscolar`),
  CONSTRAINT `fk_matricula_alumnos1` FOREIGN KEY (`alumnos_idalumnos`) REFERENCES `alumnos` (`idalumnos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_periodoEscolar1` FOREIGN KEY (`periodoEscolar_idperiodoEscolar`) REFERENCES `periodoEscolar` (`idperiodoEscolar`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matricula`
--

LOCK TABLES `matricula` WRITE;
/*!40000 ALTER TABLE `matricula` DISABLE KEYS */;
INSERT INTO `matricula` VALUES (1,1,1),(2,2,1);
/*!40000 ALTER TABLE `matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `periodoEscolar`
--

DROP TABLE IF EXISTS `periodoEscolar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `periodoEscolar` (
  `idperiodoEscolar` int(11) NOT NULL AUTO_INCREMENT,
  `desperiodo` varchar(45) NOT NULL,
  PRIMARY KEY (`idperiodoEscolar`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodoEscolar`
--

LOCK TABLES `periodoEscolar` WRITE;
/*!40000 ALTER TABLE `periodoEscolar` DISABLE KEYS */;
INSERT INTO `periodoEscolar` VALUES (1,'bimestral'),(2,'trimestral');
/*!40000 ALTER TABLE `periodoEscolar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salones`
--

DROP TABLE IF EXISTS `salones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salones` (
  `idsalones` int(11) NOT NULL AUTO_INCREMENT,
  `nombresalon` varchar(45) NOT NULL,
  PRIMARY KEY (`idsalones`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salones`
--

LOCK TABLES `salones` WRITE;
/*!40000 ALTER TABLE `salones` DISABLE KEYS */;
INSERT INTO `salones` VALUES (1,'primero'),(2,'segundo');
/*!40000 ALTER TABLE `salones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-11 13:54:21
