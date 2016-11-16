-- MySQL schema para a API de Processos de Software.
-- Modificada para ter uma descrição mais completa do banco de dados.
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
--
-- Database: `processodesoftware`
--
-- --------------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `processodesoftware` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `processodesoftware` ;
--
-- DROP TABLE IF EXISTS `users` ;
--
-- Estrutura da tabela `users`
--
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `idade` int(11) NOT NULL,
  `senha` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- DROP TABLE IF EXISTS `users_info` ;
--
-- Estrutura da tabela `users_info`
--
CREATE TABLE IF NOT EXISTS `users_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `facebook` varchar(100) DEFAULT NULL,
  `whatsapp` bigint(11) DEFAULT NULL,
  `id_user` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_info_user_idx`
    FOREIGN KEY (`id_user`)
    REFERENCES `processodesoftware`.`users` (`id`)
	ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
	ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
