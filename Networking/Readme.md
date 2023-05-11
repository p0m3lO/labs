# Basic networking lab for linux

## 1. Task

### SSH configuration:

1. generate an ***ssh-key*** and set key-based authentication on ***gde-server***
2. Create an ***ssh configuration*** file with a stanza (section). The host should named ***gde-server*** and configure to use the generated key
3. Test the connection eg.: ***$ ssh gde-server***
4. Configure the local ssh daemon: disable ***root login***, disable ***password authentication***

## 2. Task

### SSHFS configuration:

1. Create a directory on the ***gde-server***: ***/mnt/mount***
2. Install the sshfs package
3. Mount it on the ***lab_vm*** with sshfs command to path: ***/mnt/shared***
4. Make it ***auto-mount*** at startup
5. Use the ***ssh alias*** configured in the ***1. Task***

## 3. Task

### Create a Basic Nginx Web server

- ***Install*** Nginx web server
- ***Create*** a custom HTML welcome page with the text ***"Welcome to My GDE lab test Site!"*** in an `<h1>` element
- ***Configure*** Nginx to serve the custom welcome page as the default page, it should served from ***/var/www/gde*** directory
- ***Restart*** the Nginx service to apply the changes

## 4. Task

### Basic NFS server Task

Create an ***NFS server*** that only supports NFSv4 protocol and exports a shared directory to clients in

- Install the necessary NFS server packages.
- Create a shared directory, ***/opt/nfs/shared***
- Configure the NFS server to export the shared directory and allow only NFSv4 protocol
- Start and enable the NFS server service
- Configure the firewall to allow NFSv4 traffic

### 5. Task

### Simple Mail Server configuration

Install the ***postfix*** package, configure Postfix and ***mailutils*** to send and receive emails only within the local machine (localhost), and set the hostname to ***gdemailserver***

### 6. Task

### Simple Linux Firewall configuration

- Install iptables if it is not already installed.
- Create a ***working firewall*** and write rules to ***allow incoming connections*** to ***TCP/22,5000,7681*** port and the following ports from ***192.168.10.20*** IP address: ***TCP/80,443,2049,25***
- All ***other incoming traffic*** should be blocked
- Ensure that these rules are ***saved*** and ***persist*** across reboots. You can either use ***manual*** approach or the ***iptables-persistent*** package