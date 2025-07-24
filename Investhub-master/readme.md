# Stock Market Analysis
## TABLES
```sql
mysql> SHOW TABLES;
+-------------------+
| Tables_in_unifind |
+-------------------+
| userinfo          |
+-------------------+
```
## TABLE USERINFO
```sql
-- This is a MySQL code for creating Table userinfo
CREATE TABLE userinfo(
    userid integer primary key not null auto_increment,
    useremail varchar(100) not null,
    usercontact bigint not null,
    userage integer not null,
    username varchar(100) not null,
    userpassword varchar(100) not null
);

-- OUTPUT:
mysql> SHOW COLUMNS FROM userinfo;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| userid       | int          | NO   | PRI | NULL    | auto_increment |
| useremail    | varchar(100) | NO   |     | NULL    |                |
| usercontact  | bigint       | NO   |     | NULL    |                |
| userage      | int          | NO   |     | NULL    |                |
| username     | varchar(100) | NO   |     | NULL    |                |
| userpassword | varchar(100) | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```