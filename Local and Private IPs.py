import urllib
import re
import socket

# To Get the Local IP 
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.connect(("ipchicken.com",80))
local_ip = socket1.getsockname()[0]
socket1.close()

# To Get the Public IP
fhand = urllib.urlopen('http://ipchicken.com/')

public_ip = ''
line_count = 1

for line in fhand:
    if line_count == 51:
        public_ip = re.findall('[0-9.]+', line)
        break
    line_count += 1

# Print out Public/Private IPs
print "Public IP:", public_ip[0]
print " Local IP:", local_ip
