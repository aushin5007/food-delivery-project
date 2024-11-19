/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - django_foodfortrain
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`django_foodfortrain` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `django_foodfortrain`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can add permission',2,'add_permission'),
(5,'Can change permission',2,'change_permission'),
(6,'Can delete permission',2,'delete_permission'),
(7,'Can add group',3,'add_group'),
(8,'Can change group',3,'change_group'),
(9,'Can delete group',3,'delete_group'),
(10,'Can add user',4,'add_user'),
(11,'Can change user',4,'change_user'),
(12,'Can delete user',4,'delete_user'),
(13,'Can add content type',5,'add_contenttype'),
(14,'Can change content type',5,'change_contenttype'),
(15,'Can delete content type',5,'delete_contenttype'),
(16,'Can add session',6,'add_session'),
(17,'Can change session',6,'change_session'),
(18,'Can delete session',6,'delete_session'),
(19,'Can add assign',7,'add_assign'),
(20,'Can change assign',7,'change_assign'),
(21,'Can delete assign',7,'delete_assign'),
(22,'Can add booking',8,'add_booking'),
(23,'Can change booking',8,'change_booking'),
(24,'Can delete booking',8,'delete_booking'),
(25,'Can add delivery_boys',9,'add_delivery_boys'),
(26,'Can change delivery_boys',9,'change_delivery_boys'),
(27,'Can delete delivery_boys',9,'delete_delivery_boys'),
(28,'Can add food_category',10,'add_food_category'),
(29,'Can change food_category',10,'change_food_category'),
(30,'Can delete food_category',10,'delete_food_category'),
(31,'Can add hotels',11,'add_hotels'),
(32,'Can change hotels',11,'change_hotels'),
(33,'Can delete hotels',11,'delete_hotels'),
(34,'Can add login',12,'add_login'),
(35,'Can change login',12,'change_login'),
(36,'Can delete login',12,'delete_login'),
(37,'Can add menu',13,'add_menu'),
(38,'Can change menu',13,'change_menu'),
(39,'Can delete menu',13,'delete_menu'),
(40,'Can add passenger',14,'add_passenger'),
(41,'Can change passenger',14,'change_passenger'),
(42,'Can delete passenger',14,'delete_passenger'),
(43,'Can add payment',15,'add_payment'),
(44,'Can change payment',15,'change_payment'),
(45,'Can delete payment',15,'delete_payment'),
(46,'Can add rating',16,'add_rating'),
(47,'Can change rating',16,'change_rating'),
(48,'Can delete rating',16,'delete_rating'),
(49,'Can add reported_hotel',17,'add_reported_hotel'),
(50,'Can change reported_hotel',17,'change_reported_hotel'),
(51,'Can delete reported_hotel',17,'delete_reported_hotel'),
(52,'Can add schedule',18,'add_schedule'),
(53,'Can change schedule',18,'change_schedule'),
(54,'Can delete schedule',18,'delete_schedule'),
(55,'Can add station',19,'add_station'),
(56,'Can change station',19,'change_station'),
(57,'Can delete station',19,'delete_station'),
(58,'Can add train',20,'add_train'),
(59,'Can change train',20,'change_train'),
(60,'Can delete train',20,'delete_train'),
(61,'Can add trips',21,'add_trips'),
(62,'Can change trips',21,'change_trips'),
(63,'Can delete trips',21,'delete_trips');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'foodapp','assign'),
(8,'foodapp','booking'),
(9,'foodapp','delivery_boys'),
(10,'foodapp','food_category'),
(11,'foodapp','hotels'),
(12,'foodapp','login'),
(13,'foodapp','menu'),
(14,'foodapp','passenger'),
(15,'foodapp','payment'),
(16,'foodapp','rating'),
(17,'foodapp','reported_hotel'),
(18,'foodapp','schedule'),
(19,'foodapp','station'),
(20,'foodapp','train'),
(21,'foodapp','trips');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-03-03 08:31:45.154942'),
(2,'auth','0001_initial','2024-03-03 08:31:45.422848'),
(3,'admin','0001_initial','2024-03-03 08:31:45.491313'),
(4,'admin','0002_logentry_remove_auto_add','2024-03-03 08:31:45.498295'),
(5,'contenttypes','0002_remove_content_type_name','2024-03-03 08:31:45.533069'),
(6,'auth','0002_alter_permission_name_max_length','2024-03-03 08:31:45.545710'),
(7,'auth','0003_alter_user_email_max_length','2024-03-03 08:31:45.562020'),
(8,'auth','0004_alter_user_username_opts','2024-03-03 08:31:45.571994'),
(9,'auth','0005_alter_user_last_login_null','2024-03-03 08:31:45.589961'),
(10,'auth','0006_require_contenttypes_0002','2024-03-03 08:31:45.592955'),
(11,'auth','0007_alter_validators_add_error_messages','2024-03-03 08:31:45.602947'),
(12,'auth','0008_alter_user_username_max_length','2024-03-03 08:31:45.632898'),
(13,'auth','0009_alter_user_last_name_max_length','2024-03-03 08:31:45.649853'),
(14,'foodapp','0001_initial','2024-03-03 08:31:46.247530'),
(15,'sessions','0001_initial','2024-03-03 08:31:46.284485');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('xjvrjtrl3ls3ryhg9wom0yiy6fyve5iy','OTYwM2I0NDE1OWZjMDM2ZGFmZmFhZDg2ZDEwMDNiYjJmNmQwZTljZDp7ImxvZ2luX2lkIjoxfQ==','2024-03-19 04:12:47.712130'),
('yzt341kipztyn24577ujhv56brhg8v3u','NzY0MDJjOGQ2ZjU2OWRlMGY3MGQwYTJmZTJhYmEwZTYzMDBiYzFiNTp7ImxvZ2luX2lkIjo3LCJoaWQiOjEsInBpZCI6MX0=','2024-03-21 13:39:23.828535'),
('kg8qpjdqjta11ez1qm5hm8j63ym6waah','OWY2Nzk5NWM1YTEyMmFiMjcxNTNiYjE0NGMzYWMxNTY4MjRmZmYwYzp7ImxvZ2luX2lkIjo3LCJwaWQiOjF9','2024-03-23 05:05:58.287749'),
('6ypfmrcckau849ozbayqprbd1b674xwc','OWY2Nzk5NWM1YTEyMmFiMjcxNTNiYjE0NGMzYWMxNTY4MjRmZmYwYzp7ImxvZ2luX2lkIjo3LCJwaWQiOjF9','2024-03-23 06:17:58.077965'),
('b3p72ggylgxvpmp5t4r06k65iozfn0qs','OWY2Nzk5NWM1YTEyMmFiMjcxNTNiYjE0NGMzYWMxNTY4MjRmZmYwYzp7ImxvZ2luX2lkIjo3LCJwaWQiOjF9','2024-03-25 08:30:20.831819');

/*Table structure for table `foodapp_assign` */

DROP TABLE IF EXISTS `foodapp_assign`;

CREATE TABLE `foodapp_assign` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `delivery_boys_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_assign_booking_id_c303827d` (`booking_id`),
  KEY `foodapp_assign_delivery_boys_id_cfadf27b` (`delivery_boys_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_assign` */

/*Table structure for table `foodapp_booking` */

DROP TABLE IF EXISTS `foodapp_booking`;

CREATE TABLE `foodapp_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qty` varchar(225) NOT NULL,
  `date_time` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `menu_id` int(11) NOT NULL,
  `trip_id` int(11) NOT NULL,
  `passenger_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_booking_menu_id_fef7b2be` (`menu_id`),
  KEY `foodapp_booking_trip_id_9f55166e` (`trip_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_booking` */

insert  into `foodapp_booking`(`id`,`qty`,`date_time`,`status`,`menu_id`,`trip_id`,`passenger_id`,`price`) values 
(1,'2','<built-in method today of type object at 0x0000000076220740>','pending',1,3,1,0),
(2,'5','<built-in method today of type object at 0x0000000076220740>','pending',1,4,1,0),
(3,'544','<built-in method today of type object at 0x0000000076220740>','pending',1,3,1,0);

/*Table structure for table `foodapp_delivery_boys` */

DROP TABLE IF EXISTS `foodapp_delivery_boys`;

CREATE TABLE `foodapp_delivery_boys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `hname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_delivery_boys_hotel_id_92cc630b` (`hotel_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_delivery_boys` */

insert  into `foodapp_delivery_boys`(`id`,`fname`,`lname`,`hname`,`place`,`phone`,`email`,`hotel_id`,`login_id`) values 
(1,'ashwin','m','mm house','thayineridd','9867548692','thayineri@gmail.com',1,NULL);

/*Table structure for table `foodapp_food_category` */

DROP TABLE IF EXISTS `foodapp_food_category`;

CREATE TABLE `foodapp_food_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_food_category` */

insert  into `foodapp_food_category`(`id`,`category`) values 
(1,'chickrn'),
(3,'fried');

/*Table structure for table `foodapp_hotels` */

DROP TABLE IF EXISTS `foodapp_hotels`;

CREATE TABLE `foodapp_hotels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_name` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `login_id` int(11) NOT NULL,
  `station_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_hotels_login_id_e9150028` (`login_id`),
  KEY `foodapp_hotels_station_id_be0b30c0` (`station_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_hotels` */

insert  into `foodapp_hotels`(`id`,`hotel_name`,`phone`,`email`,`status`,`login_id`,`station_id`) values 
(1,'coffeee house','9867548692','coffee@gmail.com','accept',3,1);

/*Table structure for table `foodapp_login` */

DROP TABLE IF EXISTS `foodapp_login`;

CREATE TABLE `foodapp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_login` */

insert  into `foodapp_login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'Hotelllll12','Hotel','hotel'),
(3,'CoffeeeHouse12','Coffeeeee','hotel'),
(4,'center','Ashwin123','dboy'),
(5,'Anjanaaaa','Anjanna1232','user'),
(7,'M','M','user');

/*Table structure for table `foodapp_menu` */

DROP TABLE IF EXISTS `foodapp_menu`;

CREATE TABLE `foodapp_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `food_name` varchar(225) NOT NULL,
  `image` varchar(225) NOT NULL,
  `price` varchar(225) NOT NULL,
  `quantity` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `category_id` int(11) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_menu_category_id_a295d627` (`category_id`),
  KEY `foodapp_menu_hotel_id_2b374b1c` (`hotel_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_menu` */

insert  into `foodapp_menu`(`id`,`food_name`,`image`,`price`,`quantity`,`status`,`category_id`,`hotel_id`) values 
(1,'vgvgvv','lem_F4KXjGC.png','850','5','pending',3,1),
(2,'vgvgvv','lem_7PSb7yd.png','850','5','pending',3,1);

/*Table structure for table `foodapp_passenger` */

DROP TABLE IF EXISTS `foodapp_passenger`;

CREATE TABLE `foodapp_passenger` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `hname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `pincode` varchar(225) NOT NULL,
  `gender` varchar(225) NOT NULL,
  `age` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_passenger_login_id_37c4f24a` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_passenger` */

insert  into `foodapp_passenger`(`id`,`fname`,`lname`,`hname`,`place`,`pincode`,`gender`,`age`,`phone`,`email`,`login_id`) values 
(1,'mini','m','mm house','kochi','678999','female','26','6998759985','mini@gmal.com',7);

/*Table structure for table `foodapp_payment` */

DROP TABLE IF EXISTS `foodapp_payment`;

CREATE TABLE `foodapp_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tdate` varchar(225) NOT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_payment_booking_id_e2ba7550` (`booking_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_payment` */

/*Table structure for table `foodapp_rating` */

DROP TABLE IF EXISTS `foodapp_rating`;

CREATE TABLE `foodapp_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rate` varchar(225) NOT NULL,
  `review` varchar(225) NOT NULL,
  `date_time` varchar(225) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  `passenger_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_rating_hotel_id_d6100a38` (`hotel_id`),
  KEY `foodapp_rating_passenger_id_edb818b2` (`passenger_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_rating` */

insert  into `foodapp_rating`(`id`,`rate`,`review`,`date_time`,`hotel_id`,`passenger_id`) values 
(1,'4','jhhhn\r\n','2024-03-07',1,1),
(2,'5','jhhhn\r\n','2024-03-07',1,1),
(3,'2','njns','2024-03-07',1,1),
(4,'3','nrjn\r\n','2024-03-11',1,1);

/*Table structure for table `foodapp_reported_hotel` */

DROP TABLE IF EXISTS `foodapp_reported_hotel`;

CREATE TABLE `foodapp_reported_hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason_details` varchar(225) NOT NULL,
  `date_time` varchar(225) NOT NULL,
  `hotel_id` int(11) NOT NULL,
  `passenger_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_reported_hotel_hotel_id_8cfb5771` (`hotel_id`),
  KEY `foodapp_reported_hotel_passenger_id_55929eb3` (`passenger_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_reported_hotel` */

insert  into `foodapp_reported_hotel`(`id`,`reason_details`,`date_time`,`hotel_id`,`passenger_id`) values 
(1,'swd','2024-03-09',1,1),
(2,'vhjvkbxsn','2024-03-11',1,1);

/*Table structure for table `foodapp_schedule` */

DROP TABLE IF EXISTS `foodapp_schedule`;

CREATE TABLE `foodapp_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `arrivaltime` varchar(225) NOT NULL,
  `departuretime` varchar(225) NOT NULL,
  `stopstation_id_id` int(11) NOT NULL,
  `train_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_schedule_stopstation_id_id_a7da5544` (`stopstation_id_id`),
  KEY `foodapp_schedule_train_id_id_5aa5c5b7` (`train_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_schedule` */

insert  into `foodapp_schedule`(`id`,`arrivaltime`,`departuretime`,`stopstation_id_id`,`train_id_id`) values 
(1,'13:56','15:58',1,2);

/*Table structure for table `foodapp_station` */

DROP TABLE IF EXISTS `foodapp_station`;

CREATE TABLE `foodapp_station` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `district` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_station` */

insert  into `foodapp_station`(`id`,`sname`,`place`,`district`) values 
(1,'payyanur','thayineri','Kannur'),
(3,'uhhuh','jjjjj','idukki');

/*Table structure for table `foodapp_train` */

DROP TABLE IF EXISTS `foodapp_train`;

CREATE TABLE `foodapp_train` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `train_name` varchar(225) NOT NULL,
  `ending_station_id` int(11) NOT NULL,
  `starting_station_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_train_ending_station_id_1cb7b0aa` (`ending_station_id`),
  KEY `foodapp_train_starting_station_id_702c0937` (`starting_station_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_train` */

insert  into `foodapp_train`(`id`,`train_name`,`ending_station_id`,`starting_station_id`) values 
(2,'knmq',3,1),
(3,'jjjiji',1,3);

/*Table structure for table `foodapp_trips` */

DROP TABLE IF EXISTS `foodapp_trips`;

CREATE TABLE `foodapp_trips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tdate` varchar(225) NOT NULL,
  `passenger_id` int(11) NOT NULL,
  `train_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodapp_trips_passenger_id_5e9bc2bb` (`passenger_id`),
  KEY `foodapp_trips_train_id_a1f4b2f3` (`train_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `foodapp_trips` */

insert  into `foodapp_trips`(`id`,`tdate`,`passenger_id`,`train_id`) values 
(3,'2024-03-07',1,2),
(4,'2024-03-07',1,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
