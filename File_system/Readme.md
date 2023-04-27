# Basic File system lab for linux

## 1. Task

### Basic LVM configuration Task

Do an LVM installation using two disks, created with ***1 GB loopback devices***. The goal is to create appropriate physical volumes (PV), a volume group (VG), and a logical volume (LV). We will format the filesystem as ext4 and mount it via fstab

- Prepare the physical disks: ***/dev/loop1*** and ***/dev/loop2*** available for the LVM setup

- Create physical volumes: Set up the two disks as physical volumes using the pvcreate command.

- Create a volume group: Combine the physical volumes into a volume group using the vgcreate command.

- Create a logical volume: Create a logical volume within the volume group using the lvcreate command.

- Create a filesystem: Format the logical volume with the desired filesystem type (e.g., ext4) using the mkfs command.

- Mount the filesystem: Create a mount point (e.g., /mnt/lvm) and mount the logical volume to the mount point using the mount command.

- Add an fstab entry: Edit the /etc/fstab file to include an entry for the logical volume, specifying the mount point and filesystem type. 

## 2. Task

### Basic RAID configuration Task

Create two ***1GB loopback device***, and then create a RAID-1 (mirrored) array with those devices. The loop devices should be ***loop3*** and ***loop4***


### 3. Task

### Create a chroot environment and install a minimal Debian system

Create a directory called ***gde_chroot*** in the '/tmp' folder and install a ***minimal Debian buster system*** into that directory