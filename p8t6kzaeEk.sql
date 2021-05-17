-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 14, 2021 at 07:42 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `p8t6kzaeEk`
--

-- --------------------------------------------------------

--
-- Table structure for table `furniture`
--

CREATE TABLE `furniture` (
  `catogory` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `product` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `original_cost` varchar(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `selling_cost` varchar(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `image_url` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `no_of_items` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sold_items` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `discription` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `feedback` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `furniture`
--

INSERT INTO `furniture` (`catogory`, `product`, `original_cost`, `selling_cost`, `image_url`, `no_of_items`, `sold_items`, `discription`, `feedback`) VALUES
('Outdoor', 'GARDEN UMBRELLA', '800', '100', 'https://5.imimg.com/data5/CJ/SC/MY-3705805/garden-umbrella-500x500.jpg', '5', '0', 'polythene cover, manual installation', NULL),
('WorkStation', 'CABINETS', '3000', '500', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKgsXg63PT8pCo6mxbTGKypN2X4IhlyYhl9Q&usqp=CAU', '5', '0', '2 meter height, 6 layers, carpenter assembly', 'tejaswi-good product/'),
('WorkStation', 'CHAIRS', '1800', '500', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDtYL5ud1ttqPNPBO_f9Oiy3Ak9vfJEIOG4A&usqp=CAU', '5', '5', 'office chairs, fabric back, customised height', NULL),
('WorkStation', 'CONFERENCE TABLE', '28000', '5500', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNyrvZPKn_wGfRD8dB7fZXsPPDlNibfeR7lQ&usqp=CAU', '5', '0', '18 seater, no chairs included, 12 feet length', NULL),
('WorkStation', 'OFFICE DESK', '10000', '3000', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREkPFUdtsRaqmCqLIdvAZMrO8qFMamtKaL2w&usqp=CAU', '5', '0', 'Chocolate brown colour, rubber wood ,carpenter assembly', NULL),
('WorkStation', 'OFFICE TABLE', '4600', '850', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjr217gZDvt5upcXPyLVnTI6-SbQKCDVZ6KA&usqp=CAU', '5', '0', 'Metal base, no assembly required', NULL),
('Outdoor', 'BARBEQUE GRILL', '1000', '150', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-4oT8H7egFGirL7_uWuEJJWc-_Dr7hTWvNg&usqp=CAU', '5', '5', 'stain less steel, 4 kg weight, manual assembly required', NULL),
('Livingroom', 'RECLINER', '4000', '700', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoWnKJGgo2hUmuaaFFXSb2-fwlIscmerKCGQ&usqp=CAU', '5', '0', '1 seater, no assembly required, velvet fabric', '171FA04207-good product/'),
('Outdoor', 'HAMMOCK', '1800', '420', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgtqcyr7fnZ0fdQqg2KCZOb5xDm6HyhaCPrTGUWmeDdgDiB0N-idptyS9-BrGvrJPLjtY&usqp=CAU', '5', '1', 'Iron base, rubber wood, no assembly required', NULL),
('Outdoor', 'SWING', '1500', '300', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHih1ov-GiUe4XcUd_XQL21egAwfCPUgWY6g&usqp=CAU', '5', '0', 'bamboo wood, no assembly required,water proof', NULL),
('Outdoor', 'WOODEN PATIO', '2500', '750', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPBWT5iVEbxh0Rq0MTQpr7yFTT4bbuhdxttQ&usqp=CAU', '5', '1', '4 seater, walnut brown colour', NULL),
('Livingroom', 'SHOWCASE', '2500', '900', 'https://www.starinteriorracks.com/images/products/wall-showcase-rack.jpg', '5', '0', 'Walnut colour, carpenter assembly', NULL),
('Livingroom', 'sofa', '40000', '6000', 'https://www.ulcdn.net/images/taxon_images/taxon/1330/taxon_col_3/Artboard_2.png', '5', '0', NULL, NULL),
('Livingroom', 'TEAPOY', '3500', '1200', 'https://images.woodenstreet.de/image/cache/data%2Fcoffee-table%2Fliddle-coffee-table-revised%2Fhoney%2Ffront-574x396.jpg', '5', '0', '18 KG, engineering wood, carpenter assembly', NULL),
('Livingroom', 'TvUnit', '25000', '1500', 'https://www.ulcdn.net/images/products/155622/product/cdf.jpg?1507801460', '5', '0', NULL, NULL),
('HomeDecor', 'BOOK SHELF', '3500', '1500', 'https://www.woohome.com/wp-content/uploads/2013/11/Genius-home-decor-ideas-9-2.jpg', '5', '2', 'white plywood, carpenter assembly required', NULL),
('HomeDecor', 'CHANDELIER', '3000', '700', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwHdHOMUbAT5L0LPMd2NDqXEpcqud4YUo5bA&usqp=CAU', '5', '0', 'complete glass finish, no lights included', NULL),
('HomeDecor', 'FLOOR LAMP', '1800', '250', 'https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/productimage/2021/2/18/701441e9-cad8-407d-99bd-b84277acf48c1613640360244-1.jpg', '5', '0', '1.5 meteres height, teak wood base, foldable', NULL),
('BedRoom', 'BED', '15000', '2500', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-5430RezamgAqxD0-tIBIZYMaR4h0l2kZ2Q&usqp=CAU', '5', '5', 'Queen Size bed , engineering wood, carpenter assembly, no storage.', '19CS!0038-good product/'),
('BedRoom', 'BED LAMP', '200', '100', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEn0zapuZAeTPQ-Y35poT11oHf27ZgOWgtlQ&usqp=CAU', '5', '0', 'Pure glass, high quality, fabric cover ', 'rahul3-good product/'),
('BedRoom', 'BEDSIDE TABLE', '4000', '800', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq3bk7-zEs-nY9QqChltWBcNIm6j7uS3D5JQ&usqp=CAU', '5', '0', 'Provincial teak, no assembly required', NULL),
('BedRoom', 'DRESSING TABLE', '7000', '1200', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQsXczqvzWGNgP5-K3qpMx3epcqeV1mLzsXQ&usqp=CAU', '5', '1', 'Carpenter assembly, engineering wood', NULL),
('BedRoom', 'STUDY TABLE', '5000', '1000', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTShsl8UrdFt_a0_kNgohmxBzilD8uGWnZpTA&usqp=CAU', '5', '0', 'Engineering wood, carpenter assembly', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `MyUsers`
--

CREATE TABLE `MyUsers` (
  `username` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_pass` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Delivery_info` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone_number` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `renting_cart` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `prev_order` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pending_order` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pending_order_prices` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cart_price` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `return_cart` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dummy` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `additional` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Indexes for table `furniture`
--
ALTER TABLE `furniture`
  ADD UNIQUE KEY `product` (`product`);

--
-- Indexes for table `MyUsers`
--
ALTER TABLE `MyUsers`
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
