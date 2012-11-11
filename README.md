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

## Usage

Requirements:

- MySQL 5.1+
- Root/administritive access on the machine where MySQL is running
- Basic text-editor skills

Installing the collation is relatively simple, and doesn't require recompiling anything.
Adding a new collation does not affect any existing tables; you need to explicitly specify the collation in your create statements and/or queries in order to benefit from it.

### Instructions

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
1. Open the `Index.xml` file for editing (you will need to be root).
1. Copy the Maltese `<collation ...>` section from the correct `utf8_maltese_ci-mysql_5.x.xml` file (from this repository).
1. Paste the copied XML into the `<charset name="utf8">...</charset>` section of your `Index.xml` file.
1. Save the file and [restart the MySQL service][restart].
1. Test it (below).

[id51]:http://dev.mysql.com/doc/refman/5.1/en/adding-collation-choosing-id.html
[id55]:http://dev.mysql.com/doc/refman/5.5/en/adding-collation-choosing-id.html
[id56]:http://dev.mysql.com/doc/refman/5.6/en/adding-collation-choosing-id.html
[restart]:http://theos.in/desktop-linux/tip-that-matters/how-do-i-restart-mysql-server/


### Testing

1. Make sure the collation has been registered:  
`SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE COLLATION_NAME='utf8_maltese_ci'`
1. Create a simple test table by running `test-table.sql` (in this repository), and run the following query to ensure the collation works:  
`SELECT s FROM maltese_collation_test ORDER BY s ASC COLLATE 'utf8_maltese_ci'`
