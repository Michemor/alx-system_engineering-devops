# 0x04. Loops, conditions and parsing
#### DevOps Shell Bash Scripting


### man or help
env
cut
for
until
while
if


## General
- How to create SSH keys
Using the command:
ssh-keygen -b 4096 generates a ssh key for you

- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
Enables your script to be portable across different operating systems <br>
In different os the bash executable might not be located in the /usr/bin/ <br>
directory
- How to use while, until and for loops
for i in LIST ; do __ commands __; done
while [condition] ; do __ commands __ ; done
until [condition]; do __ commands __; done
(until works similar to loop although its condition will stop executing <br>
once it becomes true)
(The while loop condition will stop executing when it becomes false)
- How to use if, else, elif and case condition statements
if condition; then
 #executes some actions
elif condition; then
 #executes some actions
else
 #default executes
fi
- How to use the cut command
  cut - remove sections from each line of files
- What are files and other comparison operators, and how to use them
Some file operators are
	-f  regular file
	-e if file exists
	-s file size is not zero
	-d file is a directory
