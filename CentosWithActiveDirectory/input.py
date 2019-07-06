#!/usr/bin/env python3
import csv
import json
choice=0
while choice != "y":
  json_attr = {}
  json_attr['IP_ETH'] = raw_input( "Enter Client IP interface name (e.g eth0):" )
  json_attr['IP_ADD'] = raw_input( "Enter IP address client machine:" )
  json_attr['IP_PREFIX'] = raw_input( "Enter network prefix:" )
  json_attr['IP_GW'] = raw_input( "Enter gateway IP:" )
  json_attr['IP_DNS'] = raw_input( "Enter DNS IP:" )
  json_attr['IP_DOM'] = raw_input( "Enter Domain( lowercase ):" )
  json_attr['IP_HOST'] = raw_input( "Enter Active Directory hostname (lowercase):" )
  json_attr['IP_CLIENT'] = raw_input( "Enter CLient hostname without appending the domain:" )
  json_attr['IP_NTP'] = raw_input( "Enter NTP Server IP:" ) 
  print "==========================================="
  print "==========================================="
  print "Client IP interface name :", json_attr['IP_ETH']
  print "CLient Machine IP :", json_attr['IP_ADD']
  print "Network prefix :", json_attr['IP_PREFIX']
  print "Gateway IP :", json_attr['IP_GW']
  print "DNS IP :", json_attr['IP_DNS']
  print "Domain :" , json_attr['IP_DOM']
  print "Active Directory hostname :", json_attr['IP_HOST']
  print "CLient hostname :", json_attr['IP_CLIENT']
  print "NTP Server IP :", json_attr['IP_NTP']
  print "==========================================="
  print "==========================================="
  choice = raw_input( "Please confirm if the details above are correct?(y/n):" )
json_attr['IP_DOM_UPPER'] = json_attr['IP_DOM'].upper()
json_attr['IP_HOST_UPPER'] = json_attr['IP_HOST'].upper()
json_attr['IP_HOST_DOM_UPPER'] = json_attr['IP_HOST_UPPER']  + '.' + json_attr['IP_DOM_UPPER']
json_attr['IP_HOST_DOM_LOWER'] = json_attr['IP_HOST'] + '.' + json_attr['IP_DOM']
json_attr['IP_CLIENT_FQDN'] = json_attr['IP_CLIENT']  + '.' + json_attr['IP_DOM']
json_attr['IP_ADD_WITH_PREFIX'] = json_attr['IP_ADD'] + '/' + json_attr['IP_PREFIX']
json_attr['WORKGROUP'] = json_attr['IP_DOM_UPPER'].split('.',1)[0]
#print json.dumps(json_attr, indent=4, sort_keys=False)
with open('Attrib.json', 'w') as json_file:
  json.dump(json_attr, json_file)
# Read the krb template file
with open('config/krb5.conf.template', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('MY-REALM', json_attr['IP_DOM_UPPER'])
filedata = filedata.replace('MY_REALM_LOWER', json_attr['IP_DOM'])
filedata = filedata.replace('MY-FULL-REALM-UPPER', json_attr['IP_HOST_DOM_UPPER'])

# Write the file out again
with open('config/krb5.conf', 'w') as file:
  file.write(filedata)

# Read the smb template file
with open('config/smb.conf.template', 'r') as file1 :
  filedata1 = file1.read()

# Replace the target string
filedata1 = filedata1.replace('MY-REALM', json_attr['IP_DOM_UPPER'])
filedata1 = filedata1.replace('MY_WORK', json_attr['WORKGROUP'])
filedata1 = filedata1.replace('MY-FULL-REALM-UPPER', json_attr['IP_HOST_DOM_UPPER'])

# Write the file out again
with open('config/smb.conf', 'w') as file1:
  file1.write(filedata1)

# Read the sssd template file
with open('config/sssd.conf.template', 'r') as file2 :
  filedata2 = file2.read()

# Replace the target string
filedata2 = filedata2.replace('MY_REALM_LOWER', json_attr['IP_DOM'])
filedata2 = filedata2.replace('MY-FULL-REALM-LOWER', json_attr['IP_HOST_DOM_LOWER'])

# Write the file out again
with open('config/sssd.conf', 'w') as file2:
  file2.write(filedata2)

with open('inventory.ini.template', 'r') as file3 :
  filedata3 = file3.read()
filedata3 = filedata3.replace('IP_ADD',json_attr['IP_ADD'])
with open('inventory.ini', 'w') as file3:
  file3.write(filedata3)
