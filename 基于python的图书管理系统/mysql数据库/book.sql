/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50710
Source Host           : localhost:3306
Source Database       : book

Target Server Type    : MYSQL
Target Server Version : 50710
File Encoding         : 65001

Date: 2019-06-16 11:16:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin_t
-- ----------------------------
DROP TABLE IF EXISTS `admin_t`;
CREATE TABLE `admin_t` (
  `admin_num` int(11) NOT NULL,
  `admin_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`admin_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_t
-- ----------------------------
INSERT INTO `admin_t` VALUES ('1', '张迪', '111111');

-- ----------------------------
-- Table structure for book_t
-- ----------------------------
DROP TABLE IF EXISTS `book_t`;
CREATE TABLE `book_t` (
  `book_name` varchar(255) NOT NULL,
  `book_num` int(11) NOT NULL,
  `price` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `student_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`book_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of book_t
-- ----------------------------
INSERT INTO `book_t` VALUES ('软件工程概论', '1', '35￥', '王建民', '已借阅', '20163480');
INSERT INTO `book_t` VALUES ('python实战', '2', '20￥', '刘立嘉', '已借阅', '20163480');
INSERT INTO `book_t` VALUES ('软件过程与管理', '3', '20￥', '王辉', '已借阅', '20163480');
INSERT INTO `book_t` VALUES ('移动应用开发', '4', '20￥', '杨子光', '已借阅', '20163480');
INSERT INTO `book_t` VALUES ('软件测试', '5', '30￥', '刘丹', '未借阅', '0');
INSERT INTO `book_t` VALUES ('手机游戏设计', '6', '20￥', '刘辉', '未借阅', '0');
INSERT INTO `book_t` VALUES ('web界面设计', '7', '20￥', '刘莉', '未借阅', '0');
INSERT INTO `book_t` VALUES ('数学二', '8', '10', '张迪', '未借阅', '0');

-- ----------------------------
-- Table structure for student_t
-- ----------------------------
DROP TABLE IF EXISTS `student_t`;
CREATE TABLE `student_t` (
  `student_num` int(11) NOT NULL,
  `student_name` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `grade` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`student_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student_t
-- ----------------------------
INSERT INTO `student_t` VALUES ('20160404', '李赫宰', '男', '信9999-1', '111111');
INSERT INTO `student_t` VALUES ('20161015', '李东海', '男', '信9999-1', '111111');
INSERT INTO `student_t` VALUES ('20163478', '王云玲', '女', '信1605-3', '111111');
INSERT INTO `student_t` VALUES ('20163480', '张迪', '女', '信1605-1', '123456');
INSERT INTO `student_t` VALUES ('20163587', '姚雅丽', '女', '信1605-1', '111111');
