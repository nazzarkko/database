CREATE SCHEMA IF NOT EXISTS `nutrition` DEFAULT CHARACTER SET utf8 ;
USE `nutrition` ;

DROP TABLE IF EXISTS `nutrition`.`shchedule`;
DROP TABLE IF EXISTS `nutrition`.`day`;
DROP TABLE IF EXISTS `nutrition`.`dish`;
DROP TABLE IF EXISTS `nutrition`.`nutritional_suplement`;
DROP TABLE IF EXISTS `nutrition`.`trainer`;
DROP TABLE IF EXISTS `nutrition`.`sportsmen`;
DROP TABLE IF EXISTS `nutrition`.`sport`;
DROP TABLE IF EXISTS `nutrition`.`competition_past`;
DROP TABLE IF EXISTS `nutrition`.`place`;

CREATE TABLE IF NOT EXISTS `nutrition`.`place` (
  `idplace` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idplace`))
ENGINE = InnoDB;
ALTER TABLE `nutrition`.`place`
ADD INDEX `name_idx` (`name` ASC) VISIBLE,
ADD INDEX `adress_idx` (`adress` ASC) VISIBLE;


CREATE TABLE IF NOT EXISTS `nutrition`.`competition_past` (
  `idcompetitions_past` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `year` VARCHAR(45) NOT NULL,
  `place` INT NOT NULL,
  PRIMARY KEY (`idcompetitions_past`, `place`))
ENGINE = InnoDB;

ALTER TABLE `nutrition`.`competition_past`
ADD CONSTRAINT `place`
FOREIGN KEY (`place`)
REFERENCES `nutrition`.`place` (`idplace`),
ADD INDEX `name_idx_cp` (`name` ASC) VISIBLE,
ADD INDEX `year_idx` (`year` ASC) VISIBLE;

CREATE TABLE IF NOT EXISTS `nutrition`.`sport` (
  `idsport` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `team` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsport`))
ENGINE = InnoDB;
ALTER TABLE `nutrition`.`sport`
ADD INDEX `team_idx` (`team` ASC) VISIBLE,
ADD INDEX `idsport_idx` (`idsport` ASC) VISIBLE;



CREATE TABLE IF NOT EXISTS `nutrition`.`sportsmen` (
  `idsportsmen` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `sport` INT NOT NULL,
  `height` DECIMAL(5,2) NOT NULL,
  `weight` DECIMAL(4,1) NOT NULL,
  `competitions_past` INT NOT NULL,
  PRIMARY KEY (`idsportsmen`, `name`))
ENGINE = InnoDB;

ALTER TABLE `nutrition`.`sportsmen`
ADD CONSTRAINT `competition_past`
FOREIGN KEY (`competitions_past`)
REFERENCES `nutrition`.`competition_past` (`idcompetitions_past`),
ADD CONSTRAINT `sport`
FOREIGN KEY (`sport`)
REFERENCES `nutrition`.`sport` (`idsport`),
ADD INDEX `surname_idx` (`surname` ASC) VISIBLE,
ADD INDEX `height_weight_idx` (`height`, `weight` ASC) VISIBLE;


-- Table `trainer`
CREATE TABLE IF NOT EXISTS `nutrition`.`trainer` (
  `idtrainers` INT NOT NULL,
  `sport` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `sportsmen` INT NOT NULL,
  PRIMARY KEY (`idtrainers`))
ENGINE = InnoDB;

ALTER TABLE `nutrition`.`trainer`
ADD CONSTRAINT `sportsmen`
FOREIGN KEY (`sportsmen`)
REFERENCES `nutrition`.`sportsmen` (`idsportsmen`),
ADD INDEX `name_idx_tr` (`name` ASC) VISIBLE,
ADD INDEX `surname_idx_tr` (`surname` ASC) VISIBLE;


CREATE TABLE IF NOT EXISTS `nutrition`.`nutritional_suplement` (
  `idnutritional_suplements` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(150) NOT NULL,
  `effect` VARCHAR(100) NOT NULL,
  `period_of_using_in_month` INT NOT NULL,
  `count_of_day` INT NOT NULL,
  `main_component` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnutritional_suplements`))
ENGINE = InnoDB;
ALTER TABLE `nutrition`.`nutritional_suplement`
ADD INDEX `description_idx` (`description` ASC) VISIBLE,
ADD INDEX `main_component_idx` (`main_component` ASC) VISIBLE;


CREATE TABLE IF NOT EXISTS `nutrition`.`dish` (
  `iddish` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `calories` INT NOT NULL,
  PRIMARY KEY (`iddish`))
ENGINE = InnoDB;
ALTER TABLE `nutrition`.`dish`
ADD INDEX `calories_idx` (`calories` ASC) VISIBLE,
ADD INDEX `name_idx_d` (`name` ASC) VISIBLE;

CREATE TABLE IF NOT EXISTS `nutrition`.`day` (
  `idday` INT NOT NULL,
  `dish` INT NOT NULL,
  `nutrition_suplement` INT NOT NULL,
  `day` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idday`, `dish`, `nutrition_suplement`))
ENGINE = InnoDB;

ALTER TABLE `nutrition`.`day`
ADD CONSTRAINT `nutrition_suplement_d`
FOREIGN KEY (`nutrition_suplement`)
REFERENCES `nutrition`.`nutritional_suplement` (`idnutritional_suplements`),
ADD CONSTRAINT `dish_d`
FOREIGN KEY (`dish`)
REFERENCES `nutrition`.`dish` (`iddish`),
ADD INDEX `day_name_idx` (`day` ASC) VISIBLE,
ADD INDEX `dish_nutrition_idx` (`dish`, `nutrition_suplement` ASC) VISIBLE;


CREATE TABLE IF NOT EXISTS `nutrition`.`shchedule` (
  `idshcedule` INT NOT NULL,
  `day` INT NOT NULL,
  `sportsmen` INT NOT NULL,
  PRIMARY KEY (`idshcedule`, `day`, `sportsmen`))
ENGINE = InnoDB;

ALTER TABLE `nutrition`.`shchedule`
ADD CONSTRAINT `day_shchedule`
FOREIGN KEY (`day`)
REFERENCES `nutrition`.`day` (`idday`),
ADD CONSTRAINT `sportsmen_f_s`
FOREIGN KEY (`sportsmen`)
REFERENCES `nutrition`.`sportsmen` (`idsportsmen`),
ADD INDEX `idshcedule_idx` (`idshcedule` ASC) VISIBLE,
ADD INDEX `sportsmen_day_idx` (`sportsmen`, `day` ASC) VISIBLE;

INSERT INTO `nutrition`.`place` (`idplace`, `name`, `adress`) VALUES
(1, 'Place A', 'Address A'),
(2, 'Place B', 'Address B'),
(3, 'Place C', 'Address C'),
(4, 'Place D', 'Address D'),
(5, 'Place E', 'Address E'),
(6, 'Place F', 'Address F'),
(7, 'Place G', 'Address G'),
(8, 'Place H', 'Address H'),
(9, 'Place I', 'Address I'),
(10, 'Place J', 'Address J'),
(11, 'Place K', 'Address K'),
(12, 'Place L', 'Address L'),
(13, 'Place M', 'Address M'),
(14, 'Place N', 'Address N'),
(15, 'Place O', 'Address O');
INSERT INTO `nutrition`.`competition_past` (`idcompetitions_past`, `name`, `year`, `place`) VALUES
(1, 'Competition A', '2023', 1),
(2, 'Competition B', '2023', 2),
(3, 'Competition C', '2022', 3),
(4, 'Competition D', '2022', 4),
(5, 'Competition E', '2021', 5),
(6, 'Competition F', '2021', 6),
(7, 'Competition G', '2020', 7),
(8, 'Competition H', '2020', 8),
(9, 'Competition I', '2019', 9),
(10, 'Competition J', '2019', 10),
(11, 'Competition K', '2018', 11),
(12, 'Competition L', '2018', 12),
(13, 'Competition M', '2017', 13),
(14, 'Competition N', '2017', 14),
(15, 'Competition O', '2016', 15);
INSERT INTO `nutrition`.`sport` (`idsport`, `name`, `team`) VALUES
(1, 'Sport A', 'Team A'),
(2, 'Sport B', 'Team B'),
(3, 'Sport C', 'Team C'),
(4, 'Sport D', 'Team D'),
(5, 'Sport E', 'Team E'),
(6, 'Sport F', 'Team F'),
(7, 'Sport G', 'Team G'),
(8, 'Sport H', 'Team H'),
(9, 'Sport I', 'Team I'),
(10, 'Sport J', 'Team J'),
(11, 'Sport K', 'Team K'),
(12, 'Sport L', 'Team L'),
(13, 'Sport M', 'Team M'),
(14, 'Sport N', 'Team N'),
(15, 'Sport O', 'Team O');
INSERT INTO `nutrition`.`sportsmen` (`idsportsmen`, `name`, `surname`, `sport`, `height`, `weight`, `competitions_past`) VALUES
(1, 'Name A', 'Surname A', 1, 175.0, 70.0, 1),
(2, 'Name B', 'Surname B', 2, 176.0, 71.0, 2),
(3, 'Name C', 'Surname C', 3, 177.0, 72.0, 3),
(4, 'Name D', 'Surname D', 4, 178.0, 73.0, 4),
(5, 'Name E', 'Surname E', 5, 179.0, 74.0, 5),
(6, 'Name F', 'Surname F', 6, 180.0, 75.0, 6),
(7, 'Name G', 'Surname G', 7, 181.0, 76.0, 7),
(8, 'Name H', 'Surname H', 8, 182.0, 77.0, 8),
(9, 'Name I', 'Surname I', 9, 183.0, 78.0, 9),
(10, 'Name J', 'Surname J', 10, 184.0, 79.0, 10),
(11, 'Name K', 'Surname K', 11, 185.0, 80.0, 11),
(12, 'Name L', 'Surname L', 12, 186.0, 81.0, 12),
(13, 'Name M', 'Surname M', 13, 187.0, 82.0, 13),
(14, 'Name N', 'Surname N', 14, 188.0, 83.0, 14),
(15, 'Name O', 'Surname O', 15, 189.0, 84.0, 15);
INSERT INTO `nutrition`.`trainer` (`idtrainers`, `sport`, `name`, `surname`, `sportsmen`) VALUES
(1, 1, 'Trainer Name A', 'Trainer Surname A', 1),
(2, 2, 'Trainer Name B', 'Trainer Surname B', 2),
(3, 3, 'Trainer Name C', 'Trainer Surname C', 3),
(4, 4, 'Trainer Name D', 'Trainer Surname D', 4),
(5, 5, 'Trainer Name E', 'Trainer Surname E', 5),
(6, 6, 'Trainer Name F', 'Trainer Surname F', 6),
(7, 7, 'Trainer Name G', 'Trainer Surname G', 7),
(8, 8, 'Trainer Name H', 'Trainer Surname H', 8),
(9, 9, 'Trainer Name I', 'Trainer Surname I', 9),
(10, 10, 'Trainer Name J', 'Trainer Surname J', 10),
(11, 11, 'Trainer Name K', 'Trainer Surname K', 11),
(12, 12, 'Trainer Name L', 'Trainer Surname L', 12),
(13, 13, 'Trainer Name M', 'Trainer Surname M', 13),
(14, 14, 'Trainer Name N', 'Trainer Surname N', 14),
(15, 15, 'Trainer Name O', 'Trainer Surname O', 15);
INSERT INTO `nutrition`.`nutritional_suplement` (`idnutritional_suplements`, `name`, `description`, `effect`, `period_of_using_in_month`, `count_of_day`, `main_component`) VALUES
(1, 'Supplement A', 'Description A', 'Effect A', 1, 2, 'Component A'),
(2, 'Supplement B', 'Description B', 'Effect B', 2, 3, 'Component B'),
(3, 'Supplement C', 'Description C', 'Effect C', 1, 1, 'Component C'),
(4, 'Supplement D', 'Description D', 'Effect D', 2, 2, 'Component D'),
(5, 'Supplement E', 'Description E', 'Effect E', 3, 2, 'Component E'),
(6, 'Supplement F', 'Description F', 'Effect F', 1, 3, 'Component F'),
(7, 'Supplement G', 'Description G', 'Effect G', 2, 1, 'Component G'),
(8, 'Supplement H', 'Description H', 'Effect H', 3, 3, 'Component H'),
(9, 'Supplement I', 'Description I', 'Effect I', 1, 2, 'Component I'),
(10, 'Supplement J', 'Description J', 'Effect J', 2, 1, 'Component J'),
(11, 'Supplement K', 'Description K', 'Effect K', 3, 2, 'Component K'),
(12, 'Supplement L', 'Description L', 'Effect L', 1, 3, 'Component L'),
(13, 'Supplement M', 'Description M', 'Effect M', 2, 2, 'Component M'),
(14, 'Supplement N', 'Description N', 'Effect N', 3, 1, 'Component N'),
(15, 'Supplement O', 'Description O', 'Effect O', 1, 2, 'Component O');
INSERT INTO `nutrition`.`dish` (`iddish`, `name`, `calories`) VALUES
(1, 'Dish A', 200),
(2, 'Dish B', 210),
(3, 'Dish C', 220),
(4, 'Dish D', 230),
(5, 'Dish E', 240),
(6, 'Dish F', 250),
(7, 'Dish G', 260),
(8, 'Dish H', 270),
(9, 'Dish I', 280),
(10, 'Dish J', 290),
(11, 'Dish K', 300),
(12, 'Dish L', 310),
(13, 'Dish M', 320),
(14, 'Dish N', 330),
(15, 'Dish O', 340);
INSERT INTO `nutrition`.`day` (`idday`, `dish`, `nutrition_suplement`, `day`) VALUES
(1, 1, 1, 'Monday'),
(2, 2, 2, 'Tuesday'),
(3, 3, 3, 'Wednesday'),
(4, 4, 4, 'Thursday'),
(5, 5, 5, 'Friday'),
(6, 6, 6, 'Saturday'),
(7, 7, 7, 'Sunday'),
(8, 8, 8, 'Monday'),
(9, 9, 9, 'Tuesday'),
(10, 10, 10, 'Wednesday'),
(11, 11, 11, 'Thursday'),
(12, 12, 12, 'Friday'),
(13, 13, 13, 'Saturday'),
(14, 14, 14, 'Sunday'),
(15, 15, 15, 'Monday');
INSERT INTO `nutrition`.`shchedule` (`idshcedule`, `day`, `sportsmen`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15);


