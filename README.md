# Maltese MySQL Collation (`utf8_maltese_ci`)

John J. Camilleri  
September 2012

## About

This is a custom collation for MySQL which correctly sorts strings according to the Maltese alphabet:

    a b ċ d e f ġ g għ h ħ i ie j k l m n o p q r s t u v w x ż z

MySQL's `utf8_unicode_ci` collation treats **g** and **ġ** etc. as interchangeable, and `utf8_bin` places **ċ, ġ, ħ, ż** _after_ the letter **z** — neither of which is correct. 

## Notes

The current version is designed for MySQL < 5.6, and cannot handle double character sequences. So, **għ** is treated as two separate letters and is sorted _after_ the character sequence **gh**, which is strictly incorrect. This also means that **ie** would be sorted after **io**, which again is wrong.
MySQL 5.6 should have support for this, but I haven't written a collation for that version (yet).

I have only tested this with data in Maltese and English. Compatibility with characters from other languages may not be what you expect. Let me know if you find issues when your data contains other characters which don't sort well with respect to Maltese under this collation.

## Usage

Requirements:

- MySQL 5.1+
- Root/administritive access on the machine where MySQL is running
- Basic text-editor skills

Installing the collation is relatively simple, and doesn't require recompiling anything. Adding a new collation does not affect any existing tables; you need to explicitly specify the collation in your create statements and/or queries in order to benefit from it.

### Installation

1. The ID chosen for the Maltese collation is 1356. Make sure this ID is not in use on your system by running the following:  
`SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE ID=1356;`  
and making sure it turns up no results. If the ID does exist, choose another available one (in the range 1024 to 2047).
1. Find the location of MySQL's `Index.xml` file on your system file via the variable `character_sets_dir`:  
`SHOW VARIABLES LIKE 'character_sets_dir';`
1. Edit the `Index.xml` file, adding the Maltese `<collation ...>` section within `<charset name="utf8">...</charset>`.
1. Save the file and restart the MySQL service.
1. Test it (below).

### Testing

1. Make sure the collation has been registered:  
`SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE COLLATION_NAME='utf8_maltese_ci';`
1. Create a simple test table by running `test-table.sql`, and run the following query to ensure the collation works:  
`SELECT s FROM maltese_collation_test ORDER BY s COLLATE 'utf8_maltese_ci' ASC;`
