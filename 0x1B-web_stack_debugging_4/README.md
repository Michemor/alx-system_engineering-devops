# 0x1B. Web stack debugging #4
#### DevOps | SysAdmin | Scripting | Debugging

In this web stack debugging task, we used ApacheBench to simulate
HTTP requests to a web server.
We made 2000 requests with 100 requests at a time.

The aim was to test the maximum number of requests Nginx could handle.

The solution was to expand the number of requests Nginx could handle from 15
to 4096 enabling Nginx to maintain stability under pressure
