## Network Tracking Using Wireshark and Google Maps

This code project gives a visual representaion of the internet traffic from your ip address using Wireshark, this python script, and Google maps.

Using Wireshark, I captured packets from my network and saved that as **wire.pcap** in the same directory as this project.  The Python script will look for that file name.

The python script will output **test.kml**. Go to https://www.google.com/maps/d/, create a new map and import this file into that map.

# Note:

I found that Google maps will limit the input to 2000 entires of the kml file, although you can import many layers if you want to visualize a large data set.

I used a databse file *maxmind4.dat* from https://www.miyuru.lk/geoiplegacy to translate the ip addresses from the  Wireshark pcap file to geolocations. This database is regularly updated, you may want to download an update it for your use.
