import dpkt
import socket
import pygeoip
from urllib.request import urlopen
import re as r

gi = pygeoip.GeoIP('Github/WiresharkTracking/maxmind4.dat')

def main():
    f = open('Github/WiresharkTracking/wire6.pcap', 'rb')
    fs = open('Github/WiresharkTracking/test6.kml', 'w+')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
    '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc=kmlheader+plotIPs(pcap)+kmlfooter
    print(kmldoc)
    fs.write(kmldoc)
    fs.close()

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts

def getIP():
	d = str(urlopen('http://checkip.dyndns.com/')
			.read())

	return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

def retKML(dstip, srcip):
    d = str(urlopen('http://checkip.dyndns.com/').read())
    myipadd = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name(myipadd)
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

if __name__ == '__main__':
    main()