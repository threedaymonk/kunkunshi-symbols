#!/usr/bin/env python

# https://stackoverflow.com/a/11315257

import sys
from xml.etree import ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg");

def run(files):
    acc = None
    defs = None

    for filename in files:
        root = ET.parse(filename).getroot()
        if acc is None:
            for node in root.findall("*"):
                root.remove(node)
            defs = ET.SubElement(root, "defs")
            acc = root
        else:
            for node in root.findall("*"):
                defs.append(node)
    if acc is not None:
        print(ET.tostring(acc, encoding="UTF-8").decode("UTF-8"))

if __name__ == "__main__":
    run(sys.argv[1:])
