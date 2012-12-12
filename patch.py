#!/usr/bin/python

# Patch the MySQL Index.xml file by adding definition for Maltese
# 
import readline
import subprocess

print "Script for installing utf8_maltese_ci in MySQL"

# Prompt for MySQL version
version = 5.5
in_version = raw_input("MySQL version (%s): " % version)
if in_version:
    version = in_version

# Prompt for location of file
xmlfile = "/usr/share/mysql/charsets/Index.xml"
in_xmlfile = raw_input("Location of charsets file (%s): " % xmlfile)
if in_xmlfile:
    xmlfile = in_xmlfile

# Prompt to backup file
in_backup = raw_input("Backup existing file (y)? ")
if in_backup != "no":
    pass

# Check if already installed

# Execute update

# Success
print "Done"
