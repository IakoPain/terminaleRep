-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  Dim 29 mars 2020 à 17:05
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
-- Base de données :  `videoacteurs`
--

-- --------------------------------------------------------

--
-- Structure de la table `acteur`
--

DROP TABLE IF EXISTS `acteur`;
CREATE TABLE IF NOT EXISTS `acteur` (
  `idActeur` int(11) NOT NULL AUTO_INCREMENT,
  `nomActeur` varchar(50) NOT NULL,
  `prenomActeur` varchar(50) NOT NULL,
  PRIMARY KEY (`idActeur`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `acteur`
--

INSERT INTO `acteur` (`idActeur`, `nomActeur`, `prenomActeur`) VALUES
(1, 'Ford', 'Harrison'),
(2, 'Weaver', 'Sigourney'),
(3, 'Travolta', 'John'),
(4, 'Smith', 'Will'),
(5, 'Marceau', 'Sophie'),
(6, 'Snipes', 'Wesley'),
(7, 'Lhermitte', 'Thierry'),
(8, 'Roberts', 'Julia'),
(9, 'Di Caprio', 'Leonardo'),
(10, 'Gable', 'Clark'),
(11, 'Russel', 'Kurt'),
(12, 'Houston', 'Angelica');

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

DROP TABLE IF EXISTS `film`;
CREATE TABLE IF NOT EXISTS `film` (
  `idFilm` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(50) NOT NULL,
  `duree` int(11) NOT NULL,
  `idGenre` int(10) DEFAULT NULL,
  `idActeur` int(11) NOT NULL,
  PRIMARY KEY (`idFilm`),
  KEY `idGenre` (`idGenre`),
  KEY `idActeur` (`idActeur`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`idFilm`, `titre`, `duree`, `idGenre`, `idActeur`) VALUES
(1, 'Star wars 1', 117, 5, 1),
(2, 'Star wars 2', 122, 5, 1),
(3, 'Alien 3', 110, 5, 2),
(4, 'Allo maman, ici bébé', 92, 1, 3),
(5, 'Bad boys', 113, 3, 4),
(6, 'la famille Addams', 95, 1, 12),
(7, 'la fille de d artagnan', 124, 7, 5),
(8, 'blade', 116, 5, 6),
(9, 'le pere noel est une ordure', 90, 1, 7),
(10, 'new york 1997', 99, 5, 11),
(11, 'pretty woman', 114, 1, 8),
(12, 'titanic', 187, 7, 9),
(13, 'just married', 132, 1, 8),
(14, 'autant en emporte le vent', 175, 7, 10),
(15, 'indiana jones', 183, 7, 1);

-- --------------------------------------------------------

--
-- Structure de la table `genre`
--

DROP TABLE IF EXISTS `genre`;
CREATE TABLE IF NOT EXISTS `genre` (
  `idGenre` int(10) NOT NULL AUTO_INCREMENT,
  `genreFilm` varchar(50) NOT NULL,
  PRIMARY KEY (`idGenre`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `genre`
--

INSERT INTO `genre` (`idGenre`, `genreFilm`) VALUES
(1, 'Comedie'),
(2, 'Drame'),
(3, 'Policier'),
(4, 'Western'),
(5, 'Science-fiction'),
(6, 'Dessin animé'),
(7, 'Aventure');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `film_ibfk_1` FOREIGN KEY (`idGenre`) REFERENCES `genre` (`idGenre`),
  ADD CONSTRAINT `film_ibfk_2` FOREIGN KEY (`idActeur`) REFERENCES `acteur` (`idActeur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
