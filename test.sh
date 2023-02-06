#!/bin/sh
wget "https://raw.githubusercontent.com/free-greek-iptv/greek-iptv/master/android.m3u"
sed -e "/#EXTM3U/d" -e "s/.*,/Channel name:/" -e "s/^http/URL1:http/" -e "s/https/http/g"  "android.m3u" > "WebTV List.txt"
echo "Channel name:Ert Sports\nURL1:http://195.226.218.10/vid/ertsports/mpeg.2ts\nChannel name:Ert Sports2\nURL1:http://195.226.218.164/vid/ertplay2/mpeg.2ts\nChannel name:Ert Sports3\nURL1:http://195.226.218.164/vid/ertplay3/mpeg.2ts\nChannel name:Ert Sports4\nURL1:http://195.226.218.164/vid/ertplay4/mpeg.2ts\nChannel name:Ert Sports5\nURL1:http://195.226.218.164/vid/ertplay5/mpeg.2ts\nChannel name:Ert Sports6\nURL1:http://195.226.218.160/vid/ertplay6/mpeg.2ts\nChannel name:Ert world\nURL1:http://195.226.218.160/vid/ertworld/mpeg.2ts\nChannel name:ErtNews2\nURL1:http://195.226.218.163/vid/ertnews2/mpeg.2ts" >> "WebTV List.txt"
echo "Channel name:`date -u`\nURL1:http//www.dummytest.org.gr" >> "WebTV List.txt"
rm -rf android.m3u
