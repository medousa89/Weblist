#!/bin/sh
wget "https://raw.githubusercontent.com/free-greek-iptv/greek-iptv/master/Greekstreamtv.m3u"
sed -e "/#EXTM3U/d" -e "s/.*,/Channel name:/" -e "s/^http/URL1:http/" -e "s/https/http/g"  "Greekstreamtv.m3u" > "WebTV List.txt"
echo "Channel name:`date -u`\nURL1:http//www.A `git rev-list --all --count`" >> "WebTV List.txt"
echo "Channel name:`git rev-list --count HEAD`" >> "WebTV List.txt"
echo "URL1:http//www.A.org" >> "WebTV List.txt"
rm -rf Greekstreamtv.m3u
