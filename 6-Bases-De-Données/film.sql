-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 28 mars 2020 à 16:21
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `videotheque`
--

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

DROP TABLE IF EXISTS `film`;
CREATE TABLE IF NOT EXISTS `film` (
  `idFilm` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(50) NOT NULL,
  `duree` int(11) NOT NULL,
  `genre` varchar(50) NOT NULL,
  PRIMARY KEY (`idFilm`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`idFilm`, `titre`, `duree`, `genre`) VALUES
(1, 'Star wars 1', 117, 'Science-fiction'),
(2, 'Star wars 2', 122, 'Science-fiction'),
(3, 'Alien 3', 110, 'Science-fiction'),
(4, 'Allo maman, ici bébé', 92, 'Comedie'),
(5, 'Bad boys', 113, 'Policier'),
(6, 'la famille Addams', 95, 'Comedie'),
(7, 'la fille de d artagnan', 124, 'Aventure'),
(8, 'blade', 116, 'Science-fiction'),
(9, 'le pere noel est une ordure', 90, 'Comedie'),
(10, 'new york 1997', 99, 'Science-fiction'),
(11, 'pretty woman', 114, 'Comedie'),
(12, 'titanic', 187, 'Aventure'),
(13, 'just married', 132, 'Comedie'),
(14, 'autant en emporte le vent', 175, 'Aventure'),
(15, 'indiana jones', 183, 'Aventure');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
