# Basic lab for linux

## 1. Task

### Basic file creation Task

 Create a directory named ***gde*** inside the ***home directory*** and put a file called ***gde.txt*** into it with content: ***"This is a test"***

## 2. Task

### Basic permission Task

Create a new directory called ***test*** inside the home directory with specific permissions ***755***

## 3. Task

### Basic user create Task

Create a user ***gde*** create a new group ***student*** and add gde user to the new ***student*** group and also to the ***sudo*** group

## 4. Task

### Basic hostname change Task

Change the server hostname permanently to ***gde-lab***

## 5. Task

### Basic package management Task

Install the ***htop*** package using your ***apt package manager***

## 6. Task

### Basic symbolic link Task

Create a ***symbolic link*** named ***gde_link*** in the ***home directory*** that points to the  ***/tmp/testdir*** directory.

## 7. Task

### Basic cron job Task

Create a ***cron job*** that runs ***every 2 minutes*** and appends the current date and time to a file called 'timestamps.txt' in the '/tmp' directory.

### 8. Task

### Simple Find usage

1. Find all ***.log*** files inside ***/var/log*** directory and its subdirectories that are larger than ***10 kilobytes*** and have been modified within the ***last 7 days*** and save the output to a log file called ***/tmp/first_output.log*** inside the home directory.

2. Create some random directory and files in the user home directory (use a script for that). Find all directories in the user home directory: exclude the ***hidden directories***, and save  them to file called ***/tmp/second_output.log***. The output inside this log file should follow this format:
    ***found directory: ./<dirname> (4.0K)***
    ***found directory: ./<dirname2> (8.0K)***
    ***found directory: ./<dirname3> (16.0K)***

### 9. Task

### Simple localization configuration

Configure the server's ***localization settings*** for the ***Hungarian language***

### 10. Task

### Simple ntp configuration

Set the ***date*** with the date command. Configure NTP (Network Time Protocol) on the server. Set the server's ***timezone*** to ***Europe/Budapest*** and then install the ***chrony*** or ***ntp*** package  and configure it to use public NTP servers.

### 11. Task

### Basic screen usage

Install ***screen package*** and use screen to create a sessin called ***demo_screen*** and then run a script continuously called ***screen_test.sh***  in a detached session.

