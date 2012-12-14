# Maltese MySQL Collation (`utf8_maltese_ci`)

By _John J. Camilleri_

## About

This is a custom collation for MySQL which correctly sorts strings according to the Maltese alphabet:

    a b ċ d e f ġ g għ h ħ i ie j k l m n o p q r s t u v w x ż z

MySQL's `utf8_unicode_ci` collation treats **g** and **ġ** etc. as interchangeable, and `utf8_bin` places **ċ, ġ, ħ, ż** _after_ the letter **z** — neither of which is correct.
This collation was written to provide a solution to this.

## Notes

- Prior to version MySQL 5.6, collations cannot handle double character sequences.
So, **għ** is treated as two separate letters and is sorted _after_ the character sequence **gh**, which is strictly incorrect.
This also means that **ie** would be sorted after **io**, which again is wrong.

- I have only tested this with data in Maltese and English.
Compatibility with characters from other languages may not be what you expect.
Let me know if you find issues when your data contains other characters which don't sort well with respect to Maltese under this collation.

## Installation

### Requirements

- MySQL 5.1+
- Root/administritive access on the machine where MySQL is running
- Basic command line, text-editor, and MySQL skills

Installing the collation is relatively simple. It doesn't require recompiling anything, however you will require administrative access on your machine.
Adding a new collation does not affect any existing tables; you need to explicitly specify the collation in your create statements and/or queries in order to benefit from it.

### 1. Preparation

1. Identify your exact MySQL version with the command `SHOW VARIABLES LIKE 'version'`
1. Find an available collation ID on your MySQL server by following the steps here:
[5.1][id51], [5.5][id55], [5.6][id56].  
The IDs I chose for the Maltese collation are 225 and 1356 for MySQL 5.1 and 5.5+ respectively.
However you should make sure the chosen ID is not in use on your system by running the following:  
`SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE ID=1356`  
and making sure it turns up no results.
1. Find the location of MySQL's `Index.xml` file on your system with the command  
`SHOW VARIABLES LIKE 'character_sets_dir'`  
On an Ubuntu system this returns `/usr/share/mysql/charsets/`

[id51]:http://dev.mysql.com/doc/refman/5.1/en/adding-collation-choosing-id.html
[id55]:http://dev.mysql.com/doc/refman/5.5/en/adding-collation-choosing-id.html
[id56]:http://dev.mysql.com/doc/refman/5.6/en/adding-collation-choosing-id.html

### 2. Installation

#### Script-based installation

An install script is provided which will automatically patch your `Index.xml` file for you (you will first need the details above). Here is an example of it in use:

```bash
$ make install
sudo ./install.py
[sudo] password for user: 
Script for installing utf8_maltese_ci in MySQL
MySQL version (5.5): ↵
Location of charsets file (/usr/share/mysql/charsets/Index.xml): ↵
Backup existing file [Y/n]? ↵
Backed up to Index.xml.bak
Done
```

Notes about the install script:

- You will require Python ≥ 2.5
- If you do not have Python's `lxml` library installed, you will lose any XML comments in your `Index.xml` file.

There is also a corresonding uninstall script, which can be invoked using `make uninstall`.

#### Manual installation

If the script above doesn't work for you (or you just want to do things manually) follow these steps:

1. Open the `Index.xml` file in a text editor (you will need to be root).
1. Copy the Maltese `<collation ...>` section from the correct `utf8_maltese_ci-mysql_5.x.xml` file for your version of MySQL.
1. Paste the copied XML into the `<charset name="utf8">...</charset>` section of your `Index.xml` file.
1. Save the file and exit.

### 3. Restart MySQL

On a Unix system you can usually restart MySQL in one of the following ways:

- `service mysql restart`
- `service mysqld restart`
- `/etc/init.d/mysql restart`
- `/etc/init.d/mysqld restart`

### 4. Testing

1. Make sure the collation has been registered:  
`SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE COLLATION_NAME='utf8_maltese_ci'`
1. Create a simple test table by running `test-table.sql` (in this repository)
1. Run the following query and check how the results are sorted to ensure the collation works:  
`SELECT s FROM maltese_collation_test ORDER BY s ASC COLLATE 'utf8_maltese_ci'`
