#!/bin/sh
rm -rf userbouquet.*.tv
wget "http://sgcpm.com/livestream/stream.xml"
python3 new.py
python3 new1.py
rm -rf stream.xml
