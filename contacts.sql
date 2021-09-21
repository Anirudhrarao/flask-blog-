-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 21, 2021 at 05:04 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `annidevblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(12) NOT NULL,
  `msg` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `email`, `date`) VALUES
(42, 'deppak rao', '1234567897', 'defdafdf', 'raorudhra@gmail.com', '2021-09-17'),
(50, 'deppak rao', '1234567897', 'erghregregregreg', 'raorudhra@gmail.com', '2021-09-20'),
(52, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(53, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(54, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(55, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(56, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(57, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(58, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(59, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(60, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(61, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(63, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(64, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(65, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(66, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(67, 'deppak rao', '1234567897', 'ththththt', 'raorudhra@gmail.com', '2021-09-21'),
(68, 'anni', '1234567897', 'hello world\r\n', 'raorudhra@gmail.com', '2021-09-21'),
(69, 'deepak rao', '1234567897', 'hello', 'raorudhra@gmail.com', '2021-09-21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
