CREATE TABLE `maltese_collation_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
INSERT INTO `maltese_collation_test` (`s`) VALUES ('a');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('b');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ca');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ċe');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('d');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('e');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('f');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ġu');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ga');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ho');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ħa');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('i');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ie');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('w');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('x');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('z');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ż');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('għa');
INSERT INTO `maltese_collation_test` (`s`) VALUES ('ghe');

