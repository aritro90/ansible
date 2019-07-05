#!/usr/bin/env python3
import csv
import json
choice=0
while choice != "y":
  IP_ETH = raw_input( "Enter Client IP interface name (e.g eth0):" )
  IP_ADD = raw_input( "Enter IP address client machine:" )
  IP_PREFIX = raw_input( "Enter network prefix:" )
  IP_GW = raw_input( "Enter gateway IP:" )
  IP_DNS = raw_input( "Enter DNS IP:" )
  IP_DOM = raw_input( "Enter Domain( lowercase ):" )
  IP_HOST = raw_input( "Enter Active Directory hostname (lowercase):" )
  IP_CLIENT = raw_input( "Enter CLient hostname without appending the domain:" )
  IP_NTP = raw_input( "Enter NTP Server IP:" ) 
  print "==========================================="
  print "==========================================="
  print "Client IP interface name :", IP_ETH
  print "CLient Machine IP :", IP_ADD
  print "Network prefix :", IP_PREFIX
  print "Gateway IP :", IP_GW
  print "DNS IP :", IP_DNS
  print "Domain :" , IP_DOM
  print "Active Directory hostname :", IP_HOST
  print "CLient hostname :", IP_CLIENT
  print "NTP Server IP :", IP_NTP
  print "==========================================="
  print "==========================================="
  choice = raw_input( "Please confirm if the details above are correct?(y/n):" )
json_attr = {}
json_attr['IP_ETH'] = IP_ETH
json_attr['IP_ADD'] = IP_ADD
json_attr['IP_PREFIX'] = IP_PREFIX
json_attr['IP_GW'] = IP_GW
json_attr['IP_DNS'] = IP_DNS
json_attr['IP_DOM'] = IP_DOM
json_attr['IP_HOST'] = IP_HOST
json_attr['IP_CLIENT'] = IP_CLIENT
json_attr['IP_NTP'] = IP_NTP
json_attr['IP_DOM_UPPER'] = IP_DOM.upper()
json_attr['IP_HOST_UPPER'] = IP_HOST.upper()
json_attr['IP_HOST_DOM_UPPER'] = json_attr['IP_HOST_UPPER']  + '.' + json_attr['IP_DOM_UPPER']
json_attr['IP_CLIENT_FQDN'] = json_attr['IP_CLIENT']  + '.' + json_attr['IP_DOM']
json_attr['IP_ADD_WITH_PREFIX'] = json_attr['IP_ADD'] + '/' + json_attr['IP_PREFIX']
#print json.dumps(json_attr, indent=4, sort_keys=False)
with open('Attrib.json', 'w') as json_file:
  json.dump(json_attr, json_file)

