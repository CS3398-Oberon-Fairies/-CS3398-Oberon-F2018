-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 29, 2018 at 11:37 PM
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

-- --------------------------------------------------------

--
-- Table structure for table `parkinglot`
--

CREATE TABLE `parkinglot` (
  `Lot_id` smallint(3) NOT NULL,
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

INSERT INTO `parkinglot` (`Lot_id`, `LotName`, `SpacesTotal`, `SpacesLeft`, `Latitude`, `Longitude`, `Full`) VALUES
(1, 'Coliseum Lot (P9)', 819, 819, 29.8899078, -97.9297984, 0),
(2, '105-Admissions', NULL, NULL, 29.88629, -97.94254, 0),
(3, '106-Tower Garage', NULL, NULL, 29.8870256, -97.94264587, 0),
(4, '108-Wood St Garage', NULL, NULL, 29.88751565, -97.94395544, 0),
(5, '112-San Jacinto Hall', NULL, NULL, 29.88676, -97.94385, 0),
(6, '113-Matthews Street Garage', NULL, NULL, 29.89079995, -97.94392305, 0),
(7, '202-College Inn', NULL, NULL, 29.88933, -97.94643, 0),
(8, '203-Hornsby Hall', NULL, NULL, 29.890287, -97.942012, 0),
(9, '204-Jackson Rear', NULL, NULL, 29.88997, -97.94467, 0),
(10, '303-Blanco Garage', NULL, NULL, 29.8871625, -97.95306674, 0),
(11, '304-Academy Garage', NULL, NULL, 29.88596305, -97.94794159, 0),
(12, 'C13-Speck Garage', NULL, NULL, 29.89073725, -97.95311691, 0),
(13, 'EGS Garage', NULL, NULL, 29.8858676, -97.93972899, 0),
(14, 'Hill House Drive', NULL, NULL, 29.88925, -97.93778, 0),
(15, 'Jowers Access', NULL, NULL, 29.88734895, -97.93174999, 0),
(16, 'Old Main Drive', NULL, NULL, 29.88955, -97.93861, 0),
(17, 'P10-Bobcat Stad/East', NULL, NULL, 29.89119165, -97.92404287, 0),
(18, 'P10-Bobcat Stad/West', NULL, NULL, 29.88930285, -97.92662013, 0),
(19, 'P12-Mill St/BCV', NULL, NULL, 29.89497295, -97.92055829, 0),
(20, 'P14-Sewell North', NULL, NULL, 29.88976465, -97.93337446, 0),
(21, 'P5-Sessom Lot', NULL, NULL, 29.891219, -97.93732118, 0),
(23, 'Patient Parking/SHC', NULL, NULL, 29.89083, -97.94622, 0),
(24, 'Pickard Street', NULL, NULL, 29.8898, -97.9415, 0),
(25, 'Pleasant Street', NULL, NULL, 29.89031, -97.94077, 0),
(26, 'R11-Freeman Bldg', NULL, NULL, 29.88973, -97.93578, 0),
(27, 'R12-Music Bldg', NULL, NULL, 29.89088, -97.94074, 0),
(28, 'R13-Strahan Reserve', NULL, NULL, 29.88884845, -97.93349978, 0),
(29, 'R14-Jowers', NULL, NULL, 29.8867901, -97.933048, 0),
(30, 'R15-State Street', NULL, NULL, 29.88994, -97.93844, 0),
(31, 'R16-Aqua Sports', NULL, NULL, 29.89042, -97.93771, 0),
(32, 'R17-CDC', NULL, NULL, 29.88772, -97.94969, 0),
(33, 'R20-Supple Science', NULL, NULL, 29.88799, -97.94657, 0),
(34, 'R21-ROTC', NULL, NULL, 29.88745, -97.95011, 0),
(35, 'R23-Commons', NULL, NULL, 29.88803, -97.94019, 0),
(36, 'R2-Sessom Lot', NULL, NULL, 29.8914696, -97.93743301, 0),
(37, 'R31-SHC/Cogen', NULL, NULL, 29.89084, -97.94616, 0),
(38, 'R36-Swinney House', NULL, NULL, 29.88644, -97.94613, 0),
(39, 'R39-End Zone Complex', NULL, NULL, 29.88974215, -97.92553723, 0),
(40, 'R40-Mittie Bldg', NULL, NULL, 29.88881, -97.94698, 0),
(41, 'R41-Strahan Expansion', NULL, NULL, 29.88905575, -97.93154202, 0),
(43, 'R44-McCoy', NULL, NULL, 29.88812, -97.94477, 0),
(44, 'R4-Alkek Garage', NULL, NULL, 29.88893, -97.94308, 0),
(45, 'R5-Pleasant Garage', NULL, NULL, 29.88999785, -97.94076155, 0),
(46, 'R6-Physical Plant', NULL, NULL, 29.8911091, -97.93796346, 0),
(47, 'R-Greenhouse', NULL, NULL, 29.88613, -97.94652, 0),
(48, 'Russell Circle', NULL, NULL, 29.89062, -97.94313, 0),
(49, 'Sabinal/Colorado Bldg', NULL, NULL, 29.89116, -97.93949, 0),
(50, 'State Street', NULL, NULL, 29.88995, -97.93837, 0),
(51, 'Student Ctr Dr/Arnold', NULL, NULL, 29.88986, -97.94362, 0),
(53, 'Wood St/Education Bldg', NULL, NULL, 29.88816, -97.93906, 0),
(54, 'LBJ Student Center Parking Garage', NULL, NULL, 29.88964715, -97.94546633, 0),
(55, 'Parking Lot for Peach Tree Lofts', NULL, NULL, 29.8951988, -97.94351872, 0),
(56, 'Activity Center lot', NULL, NULL, 29.8853444, -97.9322686, 0),
(57, 'North LBJ Drive', NULL, NULL, 29.89549155, -97.94376329, 0);

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `report` tinytext NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lot_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `Token` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` bigint(20) NOT NULL,
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
  ADD PRIMARY KEY (`Lot_id`),
  ADD UNIQUE KEY `LotIdentifier_UNIQUE` (`LotName`),
  ADD UNIQUE KEY `GPS_UNIQUE` (`Latitude`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`report_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `parkinglot`
--
ALTER TABLE `parkinglot`
  MODIFY `Lot_id` smallint(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `report_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
