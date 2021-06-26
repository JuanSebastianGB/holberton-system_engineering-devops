# 0x00. Shell, basics

## Learning Objectives

### General

What does RTFM mean?
What is a Shebang
What is the Shell
What is the shell
What is the difference between a terminal and a shell
What is the shell prompt
How to use the history (the basics)

### Navigation

What do the commands or built-ins cd, pwd, ls do
How to navigate the filesystem
What are the . and .. directories
What is the working directory, how to print it and how to change it
What is the root directory
What is the home directory, and how to go there
What is the difference between the root directory and the home directory of the user root
What are the characteristics of hidden files and how to list them
What does the command cd - do

### Looking Around

What do the commands ls, less, file do
How do you use options and arguments with commands
Understand the ls long format and how to display it

### A Guided Tour

What does the ln command do
What do you find in the most common/important directories
What is a symbolic link
What is a hard link
What is the difference between a hard link and a symbolic link

### Manipulating Files

What do the commands cp, mv, rm, mkdir do
What are wildcards and how do they work
How to use wildcards
### Working with Commands

What do type, which, help, man commands do
What are the different kinds of commands
What is an alias
When do you use the command help instead of man

### Reading Man Pages

How to read a man page
What are man page sections
What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash

Common shortcuts for Bash

### LTS

What does LTS mean?


## Requirements

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long ($ wc -l file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly #!/bin/bash
- A README.md file at the root of the holberton-system_engineering-devops repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, describing what each script is doing
- You are not allowed to use backticks, &&, || or ;
- All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file. Later, we’ll learn more about how to utilize this command.

## Tasks

0. Where am I?
1. What’s in there?
2. There is no place like home
3. The long format
4. Hidden files
5. I love numbers
6. Welcome holberton
7. Betty in Holberton
8. Bye bye Betty
9. Bye bye Holberton
10. Back to the future
11. Lists
12. File type
13. We are symbols, and inhabit symbols
14. Copy HTML files
15. Let’s move
16. Clean Emacs
17. Tree
18. Life is a series of commas, not periods
19. File type: Holberton

More info

```shell
In order to run scripts we need to use change permission with chmod command
- For example using chmod +x
In order to run an script we use "./" just before the name file to run

````

## Resources

1. [What is the shell](http://linuxcommand.org/lc3_lts0010.php)
2. [Navigation](http://linuxcommand.org/lc3_lts0020.php)
3. [Looking around](http://linuxcommand.org/lc3_lts0030.php)
4. [A guided Tour](http://linuxcommand.org/lc3_lts0040.php)
5. [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
6. [Working with commands](http://linuxcommand.org/lc3_lts0060.php)
7. [Reading man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
8. [Keyboard shotcuts for bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
9. [LTS](https://wiki.ubuntu.com/LTS)
10. [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)