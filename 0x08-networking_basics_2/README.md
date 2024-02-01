# 0x08. Networking basics #1
#### DevOps Network SysAdmin

## Objectives
- What is localhost/127.0.0.1
A localhost refers to the machine the user is working from.
Each localhost has an address 127.0.0.1 that is known as a loopback address.
When used with a hostname it refers the user back to their machine.
- What is 0.0.0.0
This type of address is a special address reserved for all IPv4 addresses.
It binds a service to all network interfaces
- What is /etc/host
This is a hostfile that holds the ip-addresses and hostnames in your device.
Whenever a user searches for a website, the device checks the file whether <br>
the ip of that website has been saved and redirects the user their before <br>
surfing the network.
- How to display your machine’s active network interfaces
We can use the ifconfig command using the -a flag
