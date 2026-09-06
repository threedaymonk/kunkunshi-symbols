#!/usr/bin/env python

# https://stackoverflow.com/a/11315257

import sys
from xml.etree import ElementTree

ElementTree.register_namespace("", "http://www.w3.org/2000/svg");

def run(files):
    first = None
    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        print(ElementTree.tostring(first, encoding="UTF-8").decode("UTF-8"))

if __name__ == "__main__":
    run(sys.argv[1:])
