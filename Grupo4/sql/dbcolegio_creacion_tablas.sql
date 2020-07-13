-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: dbcolegio
-- ------------------------------------------------------
-- Server version	8.0.20


--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;

CREATE TABLE `alumno` (
  `idalumno` int NOT NULL AUTO_INCREMENT,
  `nombreAlumno` varchar(45) NOT NULL,
  `apellidoAlumno` varchar(45) NOT NULL,
  PRIMARY KEY (`idalumno`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;


--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;

CREATE TABLE `curso` (
  `idcurso` int NOT NULL AUTO_INCREMENT,
  `nombreCurso` varchar(45) NOT NULL,
  `salon_idsalon` int NOT NULL,
  PRIMARY KEY (`idcurso`),
  KEY `fk_curso_salon1_idx` (`salon_idsalon`),
  CONSTRAINT `fk_curso_salon1` FOREIGN KEY (`salon_idsalon`) REFERENCES `salon` (`idsalon`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- Table structure for table `docente`
--

DROP TABLE IF EXISTS `docente`;

CREATE TABLE `docente` (
  `iddocente` int NOT NULL AUTO_INCREMENT,
  `nombreDocente` varchar(45) NOT NULL,
  `apellidosDocente` varchar(45) NOT NULL,
  `curso_idcurso` int NOT NULL,
  PRIMARY KEY (`iddocente`),
  KEY `fk_docente_curso_idx` (`curso_idcurso`),
  CONSTRAINT `fk_docente_curso` FOREIGN KEY (`curso_idcurso`) REFERENCES `curso` (`idcurso`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- Table structure for table `notas`
--

DROP TABLE IF EXISTS `notas`;

CREATE TABLE `notas` (
  `idnotas` int NOT NULL AUTO_INCREMENT,
  `descNotas` varchar(45) NOT NULL,
  `alumno_idalumno` int NOT NULL,
  `periodo_idperiodo` int NOT NULL,
  `docente_iddocente` int NOT NULL,
  `curso_idcurso` int NOT NULL,
  PRIMARY KEY (`idnotas`),
  KEY `fk_notas_alumno1_idx` (`alumno_idalumno`),
  KEY `fk_notas_periodo1_idx` (`periodo_idperiodo`),
  KEY `fk_notas_docente1_idx` (`docente_iddocente`),
  KEY `fk_notas_curso1_idx` (`curso_idcurso`),
  CONSTRAINT `fk_notas_alumno1` FOREIGN KEY (`alumno_idalumno`) REFERENCES `alumno` (`idalumno`),
  CONSTRAINT `fk_notas_curso1` FOREIGN KEY (`curso_idcurso`) REFERENCES `curso` (`idcurso`),
  CONSTRAINT `fk_notas_docente1` FOREIGN KEY (`docente_iddocente`) REFERENCES `docente` (`iddocente`),
  CONSTRAINT `fk_notas_periodo1` FOREIGN KEY (`periodo_idperiodo`) REFERENCES `periodo` (`idperiodo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Table structure for table `periodo`
--

DROP TABLE IF EXISTS `periodo`;

CREATE TABLE `periodo` (
  `idperiodo` int NOT NULL AUTO_INCREMENT,
  `descperiodo` varchar(45) NOT NULL,
  PRIMARY KEY (`idperiodo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Table structure for table `promedio`
--

DROP TABLE IF EXISTS `promedio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promedio` (
  `idpromedio` int NOT NULL AUTO_INCREMENT,
  `descPromedio` varchar(45) NOT NULL,
  `alumno_idalumno` int NOT NULL,
  `curso_idcurso` int NOT NULL,
  PRIMARY KEY (`idpromedio`),
  KEY `fk_promedio_alumno1_idx` (`alumno_idalumno`),
  KEY `fk_promedio_curso1_idx` (`curso_idcurso`),
  CONSTRAINT `fk_promedio_alumno1` FOREIGN KEY (`alumno_idalumno`) REFERENCES `alumno` (`idalumno`),
  CONSTRAINT `fk_promedio_curso1` FOREIGN KEY (`curso_idcurso`) REFERENCES `curso` (`idcurso`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Table structure for table `salon`
--

DROP TABLE IF EXISTS `salon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salon` (
  `idsalon` int NOT NULL AUTO_INCREMENT,
  `nombreSalon` varchar(45) NOT NULL,
  PRIMARY KEY (`idsalon`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

