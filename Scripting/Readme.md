## 1. Task

### Basic grep Task

Create a Bash script named ***search.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that searches for a ***given pattern*** in a specified file. The script should accept the pattern as as the first positional parameter and the file_path as the second positional parameter. The script should be executable.

## 2. Task

### Basic redirection Task

Create a Bash script named ***redirection.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that reads input from a given file, converts all characters to uppercase using ***tr***, and writes the output to another specified file. The script should accept the input file path as the first positional parameter and the output file path as the second positional parameter. The script should be executable.

## 3. Task

### Basic find Task

Create a Bash script named ***find_files.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that searches for files with a specified name pattern in a given ***directory*** and its ***subdirectories***. The script should accept the directory path as the first positional parameter and the name pattern as the second positional parameter. The script should be executable.

## 4. Task

### Basic Tar usage

Create a Bash script named ***tar_demo.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that compresses or extracts files using the ***'tar'*** command. The script should accept three positional parameter:
    - operation mode flag (***"-c"*** for compress or ***"-x"*** for extract)
    - archive file path as the second positional parameter,
    - an optional directory path as the third positional parameter (required for compression).
The script should be executable

Example:

    ```
    $ tar_demo.sh -c example.tar.gz example/
    ```

## 5. Task

### Create a monitor script

Create a ***Bash script*** named ***monitor.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that pings a server using the IP address provided as the first positional parameter. The script should be executable.

## 6. Task

### Copy file from a remote server using SCP or RSYNC

Create a ***Bash script*** named ***remote_copy.sh*** in the ***scripts*** direcotry inside ***vagrant user home directory*** that copy log files from a remote server ***/var/log*** directory to an arbitrary local directory.

- The bash script should accept two parameter ***--age*** or -a and ***--size*** or -s
- The goal is to find log files modified in the last [n] days and bigger than [n] size
- The task can be done either via ***rsync*** or ***scp***
- The approprieate packages should be installed

Example usage for the script:

```
$ remote_copy.sh --age 7 --size 10k
```

## 6. Task

### Random directory and file creation script

Create a Bash script named ***random.sh*** in the ***scripts*** direcotry inside vagrant user ***home directory***, the script should create random ***directories*** and ***files*** inside a ***target directory***, the files should have ***random content***.

The created directories should have naming schema ***test_dir[n]*** and the created files ***file[n].txt***

***Eg.:*** test_dir1, test_dir2 and file1.txt, fil2.txt etc.

***Usage:***  ./random.sh [-d|--directory num_dirs] [-f|--files num_files] target_directory




