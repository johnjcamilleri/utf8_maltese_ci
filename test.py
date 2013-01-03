#!/usr/bin/python

# Test the Maltese collation is loaded by MySQL

import readline
import os
from shutil import copyfile
import MySQLdb

# Some globals
COLLATION = "utf8_maltese_ci"

if __name__ == "__main__":

    print "Script for checking that %s is registered in MySQL" % COLLATION

    # Get DB details
    db_host = "localhost"
    db_user = "root"
    db_pass = ""
    in_host = raw_input("MySQL hostname (%s): " % db_host)
    in_user = raw_input("Username (%s): " % db_user)
    in_pass = raw_input("Password (%s): " % db_pass)
    if in_host:
        db_host = in_host
    if in_user:
        db_user = in_user
    if in_pass:
        db_pass = in_pass

    # Connect to DB
    try:
        db = MySQLdb.connect(
            host=db_host,
            user=db_user,
            passwd=db_pass,
            db="INFORMATION_SCHEMA",
            charset="utf8"
            )
        cursor = db.cursor()
    except:
        exit("Error connecting to database")

    # Prepare & execute SQL query
    query = "SELECT * FROM INFORMATION_SCHEMA.COLLATIONS WHERE COLLATION_NAME='%s';" % COLLATION
    cursor.execute(query)

    # Check for results
    if cursor.fetchone() != None:
        print "OK"
    else:
        print "Fail"

    db.close()

