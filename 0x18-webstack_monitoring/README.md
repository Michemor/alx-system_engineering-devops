# 0x18. Webstack monitoring

#### DevOps | SysAdmin | monitoring

## Learning Objectives

### [Defined] (https://sre.google/sre-book/monitoring-distributed-systems/)

- Monitoring:
An activity that involves collecting, processing, aggregating, and displaying
real-time quantitative data about a system's performance.

### [Why] (https://sre.google/sre-book/monitoring-distributed-systems/)

1. Enables us to analyze long term trends i.e. how big is my database 
and how fast is it growing

2. We are able to make comparisons about performance over some period
and detect what caused it.

3. In the case of a crash or if the system anticipates a failure, we are
able to get alerts

4. Building dashboards which display basic information about the
service.

### Main Areas Of Monitoring

- Application monitoring: 
Getting data about your running software and making sure its behaving as expected

- Server monitoring: 
Getting data about your virtual or physical server and making sure they are not overloaded

### [NGINX Access Logs] (https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
Contains information about client requests after it is processed.
It is located at `` logs/access.log ``
The log is written to the log in a predefined __combined__ format

