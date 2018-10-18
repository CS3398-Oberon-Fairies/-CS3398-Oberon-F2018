-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 18, 2018 at 08:31 PM
-- Server version: 8.0.12
-- PHP Version: 7.3.0RC1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lots`
--
CREATE DATABASE IF NOT EXISTS `lots` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lots`;

-- --------------------------------------------------------

--
-- Table structure for table `parkinglot`
--

CREATE TABLE `parkinglot` (
  `LotName` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `SpacesTotal` int(11) DEFAULT NULL,
  `SpacesLeft` int(11) DEFAULT NULL,
  `Latitude` double NOT NULL,
  `Longitude` double NOT NULL,
  `Full` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `parkinglot`
--

INSERT INTO `parkinglot` (`LotName`, `SpacesTotal`, `SpacesLeft`, `Latitude`, `Longitude`, `Full`) VALUES
('Coliseum Lot (P9)', 819, 819, 29.8899078, -97.9297984, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Username` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Password` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `parkinglot`
--
ALTER TABLE `parkinglot`
  ADD UNIQUE KEY `LotIdentifier_UNIQUE` (`LotName`),
  ADD UNIQUE KEY `GPS_UNIQUE` (`Latitude`);
--
-- Database: `mydb`
--
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `mydb`;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
