#!/usr/bin/python

from . import _
from .stream import GreekStreamTVList
from Plugins.Plugin import PluginDescriptor
from Components.MenuList import MenuList
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Screens.Console import Console
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from os import path, listdir

GSXML = resolveFilename(SCOPE_PLUGINS, "stream.xml")
GSBQ = "userbouquet.greekstreamtv.tv"

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
                uri = uri.replace(":", "%3a")
                service = "#SERVICE {s}:0:1:{e}:{e}:0:0:0:0:0:{u}:{n}\n".format(s=serviceType, e=epgId, u=uri, n=name)
                tvlist.append((name,service))
            tvlist = sorted(tvlist, key=lambda channel: channel[0]) # sort by name
            with open(GSBQ, "w") as f:
                f.write("#NAME GreekStreamTV\n")
                for (name, service) in tvlist:
                    f.write(service)
            from enigma import eDVBDB
            eDVBDB.getInstance().reloadBouquets()
            eDVBDB.getInstance().reloadServicelist()
            tmpMessage = _("GreekStreamTV bouquet updated successfully.")
        except Exception as err:
            print("[GreekStreamTV] Exception: %s" % err)
            tmpMessage = _("GreekStreamTV bouquet update failed.")
            self.session.open(MessageBox, tmpMessage, MessageBox.TYPE_ERROR)
