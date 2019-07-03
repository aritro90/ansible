#!/bin/bash
while [ "$choice" != "y" ]
do
  echo "Enter Client IP interface name (e.g eth0)"
  read -p 'Interface name' IP_ETH
  echo Enter IP address client machine
  read -p 'IP Address: ' IP_ADD
  echo Enter network prefix
  read -p 'Prefix: ' IP_PREFIX
  echo Enter gateway IP
  read -p 'Gateway IP : ' IP_GW
  echo Enter DNS IP
  read -p 'DNS IP: ' IP_DNS
  echo "Enter Domain( lowercase )"
  read -p 'Domain: ' IP_DOM
  echo "Enter Active Directory hostname (lowercase)"
  read -p 'AD host: ' IP_HOST
  echo Enter CLient hostname without appending the domain
  read -p 'Client hostname: ' IP_CLIENT
  echo Enter NTP Server IP
  read -p 'NTP IP: ' IP_NTP
  echo "=========================================="
  echo "=========================================="
  echo "=========================================="
  echo Client IP interface name : $IP_ETH
  echo CLient Machine IP : $IP_ADD
  echo Network prefix : $IP_PREFIX
  echo Gateway IP : $IP_GW
  echo DNS IP : $IP_DNS
  echo Domain : $IP_DOM
  echo Active Directory hostname : $IP_HOST
  echo CLient hostname : $IP_CLIENT
  echo NTP Server IP: $IP_NTP
  echo "Please confirm if the details are correct?(y/n)"
  read -p '(y/n): ' choice
  echo "=========================================="
  echo "=========================================="
  echo "=========================================="
done
#this will require minimum bash 4.x in the machine
IP_DOM_UPPER=${IP_DOM^^}
IP_HOST_UPPER=${IP_HOST^^}
IP_HOST_DOM_UPPER="$IP_HOST_UPPER.$IP_DOM_UPPER"
IP_CLIENT_FQDN="$IP_CLIENT.$IP_DOM"
