# 0x05. Processes and signals
#### DevOps Shell Bash Syscall Scripting

## Learning Objectives
- What is a PID
PID which stands for process Identification number is a unique number <br> assigned to each process and is used to identify process in the kernel.<br> 
It is assigned by the kernel.
- What is a process
A process is an instance of a program
- How to find a process’ PID
PID of any process can be found out by a number of ways:
1. pidof <processname>
2. pgrep <processname>
3. In a shell session you can type: (echo $$)
4. ps - prints out the current running process with their pids in a list
- How to kill a process
The command below is passed: <br>
kill [pid] where pid stands for the process id <br>
or kill -9 [pid]
- What is a signal
A signal is an event generated by a unix and linux like system in response <br>
to a condition
- What are the 2 signals that cannot be ignored
SIGKILL and SIGSTOP
