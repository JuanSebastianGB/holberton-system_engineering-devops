# 0x01. Shell, permissions

## Learning Objectives

### Permissions

- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser

### Other Man Pages

- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

### Requirements

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long ($ wc -l file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly #!/bin/bash
- A README.md file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, &&, || or ;
- All your files must be executable

### Tasks

0. [My name is Betty](0-iam_betty) - Create a script that switches the current user to the user betty.
1. [Who am I](1-who_am_i) - Write a script that prints the effective username of the current user.
2. [Groups](2-groups) - Write a script that prints all the groups the current user is part of.
3. [New owner](3-new_owner) - Write a script that changes the owner of the file hello to the user betty.
4. [Empty!](4-empty) - Write a script that creates an empty file called hello.
5. [ Execute](5-execute) - Write a script that adds execute permission to the owner of the file hello.
6. [Multiple permissions](6-multiple_permissions) - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. [Everybody!](7-everybody) - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
8. [James Bond](8-James_Bond) - Write a script that sets the permission to the file hello as follows:
```shell
Owner: no permission at all
Group: no permission at all
Other users: all the permissions
```





### Resources

1. [Permissions](http://linuxcommand.org/lc3_lts0090.php)


