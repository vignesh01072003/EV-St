-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 01, 2023 at 10:40 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `lams1`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(50) NOT NULL auto_increment,
  `bid` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `slot` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `tamount` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `bid`, `name`, `location`, `amount`, `date`, `slot`, `uname`, `status`, `tamount`) VALUES
(1, '4', 'Smart home services', 'charthiram', '50', '2023-03-29', '12', 'admin', 'Accept', '');

-- --------------------------------------------------------

--
-- Table structure for table `bunk`
--

CREATE TABLE `bunk` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `solt` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `bunk`
--

INSERT INTO `bunk` (`id`, `name`, `city`, `location`, `solt`, `amount`) VALUES
(1, 'sam', 'trichy', 'postoffice', '12', '100000'),
(2, 'sample', 'trichy', 'annaselai', '12', '1000'),
(3, 'sample', 'trichy', 'central', '12', '122'),
(4, 'Smart home services', 'trichy', 'charthiram', '12', '50');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `gender`, `age`, `email`, `phone`, `address`, `uname`, `password`) VALUES
(1, 'sundar', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '123'),
(2, 'kumar', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '123456'),
(3, 'pandiyan', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 'pandiyan', 'p12345'),
(4, 'sundar', 'male', '29', 'sundarv06@gmail.com', '7904461622', 'trichy', 'kumar', '111'),
(5, 'sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '123456'),
(6, 'sam', 'male', '24', 'sundarv06@gmail.com', '9840234119', 'trichy', 'admin', '123'),
(7, 'admin', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin');
