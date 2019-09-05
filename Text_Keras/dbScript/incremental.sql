/*
INCREMENTAL SCRIPT FOR DB PROCESS

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100406
 Source Host           : 0.0.0.0:3306
 Source Schema         : smqdML

 Target Server Type    : MySQL
 Target Server Version : 100406
 File Encoding         : 65001

 Date: 05/09/2019 12:04:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dataclassified
-- ----------------------------
DROP TABLE IF EXISTS `dataclassified`;
CREATE TABLE `dataclassified` (
  `ProblemID` bigint(20) NOT NULL AUTO_INCREMENT,
  `Link` text DEFAULT NULL,
  `Title` text DEFAULT NULL,
  `Contexts` text DEFAULT NULL,
  `Source` text DEFAULT NULL,
  `Sentence` text DEFAULT NULL,
  `MachineClassification` text DEFAULT NULL,
  PRIMARY KEY (`ProblemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
