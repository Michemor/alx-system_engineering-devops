# 0x07. Networking basics #0
#### DevOps Network

### man or help
netstat
ping

## General
### OSI model
The OSI model is a reference system interconnection model that defines how <br>
devices connected over the network communicate
It is divided into 7 layers each handling a separate function:
- Application    - 	provides interface for user interaction
- Presentation   - 	handles data encryption, compression and encoding
- Sessions       - 	establishes, maintains, and terminates a session
- Transport	 -	handles point to point delivery of a segments
- Network	 - 	handles delivery of packets from source to <br>
			destination via the IP address
- Data Link	 - 	handles delivery of fragments from node to node <br>
			using the MAC address
- Physical	 -	responsible for transmission of data inform of bits

From the sender the physical layer is the first point of interaction.
The data travels from layer to layer at each point the data is added <br>
information until it arrives at the recepients end

### LAN
The LAN (Local Area Network) is a type of network used to connect devices over a geographical <br> range of 2km. Spans across buildings, homes, instituions or offices.

The type of technology used is the ethernet or WI-FI which offers wireless <br>
capabilities

### WAN
The WAN (Wide Area Network) which spans across countries, continets and the world.
It is typically used to connect LANs together forming a large network.
When impelemnted it enables institutions, companies, or business to continue their <br> usual tasks despite of location.

The most widely used type of WAN is the internet.

### INTERNET
The internet is a WAN that connects computers worldwide.

Assosiated with the internet is an IP address.
An IP address is a unique address assigned to each device that is connected <br> to the internet and is used to identify it.
There are two types of IP addresses:
1. IPv4 - a 32 bit address that uses decimal notation to identify devices.
2. IPv6 - a 128 bit address that uses hexadecimal notation to identify devices.

IPv4 has a possible 4 million hosts. Due to the outburst of devices connected <br> over the internet there was need for a new addressing scheme. The IPv6 was developed <br>
to overcome this limitation of IPv4 addresses.

A localhost is a hostname used to access your device using a loopback.
The localhost is an IP address; 127.0.0.1 and is reserved.
The loopback address is applied when:
- used in site blocking on a local machine
- used for testing and debugging of web applications
- also used in speed test

Subnet is a small network that has stemed from a large network through a <br>
process known as subnetting.

### TCP/UDP
The TCP/IP protocol suite built on the OSI reference model offers two <br>
protocols used for transfer of data:
- TCP (Transmission Control Protocol)
- UDP (User-Datagram Protocol)

The TCP protocol is connection-oriented in that a connection needs to be made <br> between the sender and receiver before a transfer occurs.
On the other hand, UDP is connectionless, no connection needs to be established<br> before transfer

A port is a virtual point where network connections start and end. A port is <br> assigned a unique number called a port address and port number.
Examples of port numbers include:
- For SSH 22
- For HTTP 80
- For HTTPS 443

