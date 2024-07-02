# 0x0C. Web server

#### DevOps | SysAdmin

## Objectives
The following are some key concepts surrounding this projects:

man or help:
 - curl
 - scp

curl command in full is client URL and is used to transfer files to a server.
The scp command is uses OpenSSH to securely copy files.
Both can be used to transfer files to a server.
The goal of this project is to learn how to publics web pages for a website to a web server

### WEB SERVER

A web server is a computer hardware or software that can be used to provide resources via HTTP upon request by a web browser or web crawler.
These web pages are loaded by the owner of the website.

The web server responds to requests by providing resources.

When we talk about web servers, we also need to know what a child process is. 

>> A process is reffered to as a running instance of a program. When requests are made to a server, processes, threads or event driven model are created to handle these requests. The method employed depends on the server's architecture.

>> In some server configurations, such as Apache, child processes are created to handle requests when they exceed a certain threshhold. This helps in managing the load and can prevent the web server from crashing due to an overwhelming number of requests. However, efficient load handling depends on other factors such as server configuration and load management.

### HTTP 

HTTP, which stands for HyperText Transfer Protocol, is the "language" used for communication between a web server and a web browser.
When a client or user types for a webpage in a web browser, a request is made to the server to which the server responds with the requested resource. The request and response is achieved via the HTTP protocol.

### DNS
When we continue our discourse about web servers and browsers, we have to also understand what ***DNS*** is.

DNS, Domain Name System, is used to translate domain names to the equivalent IP addresses.
Each website has a human readable name that we search it up on the on the internet.Whereas human beings use human readable text, servers use IP addresses to identify these websites.
To bridge the gap, DNS translates the domain names to IP addresses.
A domain name can be referred to as a unique indentifier of a website in text form on the internet. An example would me mycompany.com.

DNS records are instructions that reside on a DNS server and provide information about a domain name, its assosiated IP address and how to handle requests to that domain.

#### Types of DNS records
1. A record
It assosiates a particular domain name to an IP address.

2. CNAME record (Canonical record)
It assosiates domain name to another domain name.

3. MX record
Specifies the mail server responsible for accepting mail messages on behalf of a domain name

