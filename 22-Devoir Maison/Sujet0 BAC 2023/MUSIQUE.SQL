-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3307
-- Généré le : jeu. 11 avr. 2024 à 06:47
-- Version du serveur : 11.2.2-MariaDB
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `musique`
--

-- --------------------------------------------------------

--
-- Structure de la table `concerts`
--

DROP TABLE IF EXISTS `concerts`;
CREATE TABLE IF NOT EXISTS `concerts` (
  `idconc` int(2) NOT NULL,
  `scene` int(2) NOT NULL,
  `heure_debut` varchar(7) NOT NULL,
  `heure_fin` varchar(7) NOT NULL,
  `idgrp` int(2) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `concerts`
--

INSERT INTO `concerts` (`idconc`, `scene`, `heure_debut`, `heure_fin`, `idgrp`) VALUES
(10, 1, '‘20h00’', '‘20h45’', 12),
(24, 2, '’20h00’', '‘20h45’', 15),
(24, 2, '‘20h00’', '‘20h45’', 15),
(24, 2, '20h00', '20h45', 15),
(36, 1, '21h00', '22h00', 96),
(45, 3, '18h00', '18h30', 87);

-- --------------------------------------------------------

--
-- Structure de la table `groupes`
--

DROP TABLE IF EXISTS `groupes`;
CREATE TABLE IF NOT EXISTS `groupes` (
  `idgrp` int(2) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `style` varchar(25) NOT NULL,
  `nb_pers` int(2) NOT NULL,
  PRIMARY KEY (`idgrp`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `groupes`
--

INSERT INTO `groupes` (`idgrp`, `nom`, `style`, `nb_pers`) VALUES
(12, 'Weather Report', 'Latin Jazz', 5),
(25, 'Breckers Brothers', 'Swing Jazz', 4),
(87, 'Return to Forever', 'Latin Jazz', 8),
(96, 'The Jazz Messenger', 'Free Jazz', 3);

-- --------------------------------------------------------

--
-- Structure de la table `musiciens`
--

DROP TABLE IF EXISTS `musiciens`;
CREATE TABLE IF NOT EXISTS `musiciens` (
  `idmus` int(2) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `instru` varchar(25) NOT NULL,
  `idgrp` int(2) NOT NULL,
  PRIMARY KEY (`idmus`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `musiciens`
--

INSERT INTO `musiciens` (`idmus`, `nom`, `prenom`, `instru`, `idgrp`) VALUES
(12, 'Parker', 'Charlie', 'trompette', 96),
(13, 'Parker', 'Charlie', 'trombone', 25),
(58, 'Dufler', 'Candy', 'saxophone', 96),
(97, 'Miles', 'Davis', 'saxophone', 87);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
