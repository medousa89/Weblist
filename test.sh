#!/bin/sh
rm -rf stream.*.*
wget "http://sgcpm.com/livestream/stream.xml"
python3 new.py
rm -rf stream.xml
