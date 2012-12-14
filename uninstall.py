#!/usr/bin/python

# Uninstall the Maltese collation from the MySQL Index.xml

import readline
import os

try:
    import lxml.etree as ET
except ImportError:
    print("lxml not found; If you proceed you will lose all comments in your charsets XML file")
    import xml.etree.ElementTree as ET

# Some globals
COLLATION = "utf8_maltese_ci"
DEFAULT_XMLFILE = "/usr/share/mysql/charsets/Index.xml"

print "Script for uninstalling %s in MySQL" % COLLATION

# Prompt & check file location
xmlfile = DEFAULT_XMLFILE
in_xmlfile = raw_input("Location of charsets file (%s): " % xmlfile)
if in_xmlfile:
    xmlfile = in_xmlfile
if not(os.path.exists(xmlfile)):
    exit("%s does not exist" % xmlfile)

# Check if installed
tree = ET.parse(xmlfile)
node_utf8 = tree.getroot().find("charset[@name='utf8']")
node_maltese = node_utf8.find("collation[@name='%s']" % COLLATION)
if None==node_maltese:
    exit("%s is not installed in %s" % (COLLATION, xmlfile))

# Execute update
try:
    node_utf8.remove(node_maltese)
    tree.write(xmlfile, encoding="utf-8", xml_declaration=True, pretty_print=True)
except IOError as e:
    exit("Cannot write %s: %s" % (xmlfile, e.strerror))

# Success
print "Done"
