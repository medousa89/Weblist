#!/bin/sh
sed -e "/#EXTM3U/d" -e "s/.*,/Channel name:/" -e "s/^http/URL1:http/" -e "s/https/http/g"  *.m3u > "WebTV List.txt"
