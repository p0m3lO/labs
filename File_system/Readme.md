# Basic File system lab for linux

## 1. Task

### Basic LVM configuration Task

Do an LVM installation using two disks, created with ***1 GB loopback devices***. The goal is to create appropriate physical volumes (PV), a volume group (VG), and a logical volume (LV). We will format the filesystem as ext4 and mount it via fstab

- Prepare the physical disks: ***/dev/loop1*** and ***/dev/loop2*** available for the LVM setup

- Create physical volumes: Set up the two disks as physical volumes using the pvcreate command.

- Create a volume group: Combine the physical volumes into a volume group using the vgcreate command. The group name should be ***gde_group***

- Create a logical volume: Create a logical volume within the volume group using the lvcreate command. The volume name should be ***gde_volume***

- Create a filesystem: Format the logical volume with the desired filesystem type (***ext4***) using the mkfs command.

- Mount the filesystem: Create a mount point (e.g., /mnt/lvm) and mount the logical volume to the mount point using the mount command.

- Add an fstab entry: Edit the /etc/fstab file to include an entry for the logical volume, specifying the mount point and filesystem type.

- Because the lvm setup based on loop devices make sure that these devices persistent as well and mounted before the lvm device during boot

## 2. Task

### Basic RAID configuration Task

Create two ***1GB loopback device***, and then create a RAID-1 (mirrored) array with those devices. The loop devices should be ***loop3*** and ***loop4***


### 3. Task

### Create a chroot environment and install a minimal Debian system

Create a directory called ***gde_chroot*** in the '/tmp' folder and install a ***minimal Debian buster system*** into that directory

### 4. Task

### Confgiure SWAP

Create a 1GB swap file in the path ***/mnt/swap***, set it up, and configure it to be persistent across reboots

### 5. Task

### create an encrypted container using LUKS and cryptsetup

1. Install the cryptsetup package.
2. Create a 1GB file for the encrypted container called ***secret_container*** in the user home directory.
3. Format it as a LUKS container, create filesytem make it ***ext4***
4. Mount it to /mnt/secret
4. Configure ***auto-mount*** at boot with a key file and set up a mapping in ***/etc/crypttab***

