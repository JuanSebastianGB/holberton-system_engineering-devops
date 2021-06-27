# 0x02. Shell, I/O Redirections and filters

## Learning Objectives

### Shell, I/O Redirection

- What do the commands head, tail, find, wc, sort, uniq, grep, tr do
- How to redirect standard output to a file
- How to get standard input from a file instead of the keyboard
- How to send the output from one program to the input of another program
- How to combine commands and filters with redirections

### Special Characters

- What are special characters
- Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
- Other Man Pages
- How to display a line of text
- How to concatenate files and print on the standard output
- How to reverse a string
- How to remove sections from each line of files
- What is the /etc/passwd file and what is its format
- What is the /etc/shadow file and what is its format

## Requirements

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long ($ wc -l file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly #!/bin/bash
- A README.md file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, &&, || or ;
- All your files must be executable
- You are not allowed to use sed or awk

## Tasks

0. [Hello World](0-hello_world) - Write a script that prints “Hello, World”, followed by a new line to the standard output.
1. [Confused smiley](1-confused_smiley) - Write a script that displays a confused smiley "(Ôo)'.
2. [Let's display a file](2-hellofile) - Display the content of the /etc/passwd file.
3. [What about 2?](3-twofiles) - Display the content of /etc/passwd and /etc/hosts
4. [Last lines of a file](4-lastlines) - Display the last 10 lines of /etc/passwd
5. [I'd prefer the first ones actually](5-firstlines) - Display the first 10 lines of /etc/passwd
6. [Line #2](6-third_line) - Write a script that displays the third line of the file iacta.
7. [It is a good file that cuts iron without making a noise](7-file) - Write a shell script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.
8. [Save current state of directory](8-cwd_state) - Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9. [Duplicate last line](9-duplicate_last_line) - Write a script that duplicates the last line of the file iacta
10. [No more javascript](10-no_more_js) - Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
11. [Don't just count your directories, make your directories count](11-directories) - Write a script that counts the number of directories and sub-directories in the current directory.)
 - The current and parent directories should not be taken into account
 - Hidden directories should be counted 
12. [What’s new](12-newest_files) - Create a script that displays the 10 newest files in the current directory.
 - One file per line
 - Sorted from the newest to the oldest
13. [Being unique is better than being perfect](13-unique) - Create a script that takes a list of words as input and prints only words that appear exactly once.
 - Input format: One line, one word
 - Output format: One line, one word
 - Words should be sorted
14. [It must be in that file](14-findthatword) - Display lines containing the pattern “root” from the file /etc/passwd


## Resources

1. [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php)
2. [Special Characters](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)




 



