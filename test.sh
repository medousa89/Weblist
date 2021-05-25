#!/bin/sh
wget "https://raw.githubusercontent.com/free-greek-iptv/greek-iptv/master/Greekstreamtv.m3u"
sed -e "/#EXTM3U/d" -e "s/.*,/Channel name:/" -e "s/^http/URL1:http/" -e "s/https/http/g"  *.m3u > "WebTV List.txt"
