#!/usr/bin/python3
from os import path, listdir

GSXML = "stream.xml"
GSBQ = "userbouquet.greekstreamtvATV.tv"
try:
            from xml.etree.cElementTree import ElementTree
            tree = ElementTree()
            tree.parse(GSXML)
            tvlist = []
            for iptv in tree.findall("iptv"):
                name = iptv.findtext("name").title()
                (protocol, serviceType, bufferSize, epgId) = iptv.findtext("type").split(":")
                uri = iptv.findtext("uri")
                if protocol in "livestreamer":
                    uri = "http://localhost:88/" + uri
                uri = uri.replace(":88/", "%3a8088/")
                uri = uri.replace(":", "%3a")
                service = "#SERVICE {s}:0:1:{e}:{e}:0:0:0:0:0:{u}:{n}\n".format(s=serviceType, e=epgId, u=uri, n=name)
                tvlist.append((name,service))
            tvlist = sorted(tvlist, key=lambda channel: channel[0]) # sort by name
            with open(GSBQ, "w") as f:
                f.write("#NAME GreekStreamTVatv\n")
                for (name, service) in tvlist:
                    f.write(service)
except Exception as err:
            print("[GreekStreamTV] Exception: %s" % err)                    
