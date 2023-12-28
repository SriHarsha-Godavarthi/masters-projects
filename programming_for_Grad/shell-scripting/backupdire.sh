# the below line indicateds that the below line should execute with bash shell
#!/bin/bash

# Check if directory path is provided as an argument
if [ $# -eq 0 ]; then
    # $# will store no of command line arguments passed
    # $0 first word of entered command
    echo "Usage: $0 <directory_path>"
    # exit the script execution
    exit 1
fi
# pass the backup file-directory to variable
pathToBackUp=$1

# Check if input is a directory or not
if [ -d "$pathToBackUp" ]; then
    # Create  backup by compressing by having current date in the filename
    filename="backup_$(date +"%d%m%Y").tar.gz"
    # compress the directory
    tar -czvf "$filename" "$pathToBackUp"
    echo "Backup was created with fileName"
else
    # print the message if path is not directory
    echo "Error: $pathToBackUp is not a directory."
fi

# execute it cmd>./backupdire.sh <dirctory-path-to-backup>