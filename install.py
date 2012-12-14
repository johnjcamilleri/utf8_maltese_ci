#!/usr/bin/python

# Install the Maltese collation by patching the MySQL Index.xml

import readline
import os
from shutil import copyfile

try:
    import lxml.etree as ET
except ImportError:
    print("lxml not found; If you proceed you will lose all comments in your charsets XML file")
    import xml.etree.ElementTree as ET

# Some globals
COLLATION = "utf8_maltese_ci"
DEFAULT_XMLFILE = "/usr/share/mysql/charsets/Index.xml"
VERSIONS = ["5.1","5.5","5.6"]
CODEFILE_TEMPLATE = "utf8_maltese_ci-mysql_%s.xml"

print "Script for installing %s in MySQL" % COLLATION

# Prompt & check for MySQL version
version = "5.5" # note it's a string
in_version = raw_input("MySQL version (%s): " % version)
if in_version:
    version = in_version
if not(version in VERSIONS):
    exit("I only understand versions %s" % (", ".join(VERSIONS)))

# Prompt & check file location
xmlfile = DEFAULT_XMLFILE
in_xmlfile = raw_input("Location of charsets file (%s): " % xmlfile)
if in_xmlfile:
    xmlfile = in_xmlfile
if not(os.path.exists(xmlfile)):
    exit("%s does not exist" % xmlfile)

# Check if already installed
tree = ET.parse(xmlfile)
node_utf8 = tree.getroot().find("charset[@name='utf8']")
installed = None!=node_utf8.find("collation[@name='%s']" % COLLATION)
if installed:
    exit("%s is already installed in %s" % (COLLATION, xmlfile))

# Prompt to backup file
in_backup = raw_input("Backup existing file [Y/n]? ")
if in_backup != "n":
    try:
        backup_dst = "%s.bak" % os.path.basename(xmlfile)
        copyfile(xmlfile, backup_dst)
        print "Backed up to %s" % backup_dst
    except IOError as e:
        exit("Failed to back up to %s: %s" % (backup_dst, e.strerror))
else:
    print "Skipping backup"

# Execute update
codefile = CODEFILE_TEMPLATE % version
try:
    tree_maltese = ET.parse(codefile)
    node_utf8.append(tree_maltese.getroot())
    try:
        tree.write(xmlfile, encoding="utf-8", xml_declaration=True, pretty_print=True)
    except IOError as e:
        exit("Cannot write %s: %s" % (xmlfile, e.strerror))
except IOError as e:
    exit("Cannot read %s" % (codefile))

# Success
print "Done"
