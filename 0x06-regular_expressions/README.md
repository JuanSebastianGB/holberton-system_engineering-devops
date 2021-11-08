# 0x06. Regular expression

## Concepts

_For this project, students are expected to look at this concept:_

-   [Regular Expression](https://intranet.hbtn.io/concepts/29)

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the  `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```

## Resources

**Read or watch**:

-   [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg "Regular expressions - basics")
-   [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q "Regular expressions - advanced")
-   [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ "Rubular is your best friend")
-   [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw "Use a regular expression against a problem: now you have 2 problems")
-   [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A "Learn Regular Expressions with simple, interactive exercises")

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env ruby`
-   All your regex must be built for the Oniguruma library

## Tasks

### 0. Simply matching School

mandatory

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211108T054158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=87664a128a20349105667b17fbdbf9889c74a2973e044f5a3d724ce315ff415c)

Requirements:

-   The regular expression must match  `School`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `0-simply_match_school.rb`


### 1. Repetition Token #0


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211108T054158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2556834ab2c9d7c96d6dd96c63d7a329187c9855a7b203a2de000b682ba64325)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `1-repetition_token_0.rb`


### 2. Repetition Token #1



![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211108T054158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81a12469879f2b1cd8ce3a74fb74f049f11eff530f0ace6c47360d2e39271907)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `2-repetition_token_1.rb`


### 3. Repetition Token #2



![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211108T054158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=57125b64e6464f59255a6868d692d70e57352c547e64b0ed5552ac2ba39d4c13)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `3-repetition_token_2.rb`


### 4. Repetition Token #3



![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211108T054158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c60b490b43e8eeab3504b7a9a9fde6a8e1e5fae5927ad5c01ba4e8ff8b031a3e)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `4-repetition_token_3.rb`


### 5. Not quite HBTN yet



Requirements:

-   The regular expression must be exactly matching a string that starts with  `h`  ends with  `n`  and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `5-beginning_and_end.rb`


### 6. Call me maybe



This task is brought to you by a professional advisor  [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw "Neha Jain"), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `6-phone_number.rb`


### 7. OMG WHY ARE YOU SHOUTING?



![](https://intranet.hbtn.io/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

-   The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `holberton-system_engineering-devops`
-   Directory:  `0x06-regular_expressions`
-   File:  `7-OMG_WHY_ARE_YOU_SHOUTING.rb`



Copyright © 2021 Holberton Inc, All rights reserved.
