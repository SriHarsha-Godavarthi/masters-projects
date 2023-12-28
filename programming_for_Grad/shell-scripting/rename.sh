# the below line indicateds that the below line should execute with bash shell
#!/bin/bash

# Check if directory and prefix are provided as arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory> [prefix]"
    exit 1
fi
# Check if directory an prefix path is given as an argument
if [ $# -eq 0 ]; then
    # $# will store no of command line arguments passed
    # $0 first word of entered command
    echo "Usage: $0 <directory_path> "
    # exit the script execution
    exit 1
fi
# assign values to variables
directory_name=$1
file_prefix=$2
# display dirctory name and prefix
echo "dirname $directory_name"
echo "prefix $file_prefix"

# If no prefix provided, display how to execute it
# -z is used to check if a string is empty
if [ -z "$file_prefix" ]; then
    # display syntax for executing
    echo "execute it: $0 <directory> [prefix]"
    exit 1
fi

# loop through all files in directory
for file in "$directory_name"/*; do
    # Rename files in the directory with the input prefix
    mv "$file" "${directory_name}/${file_prefix}_$(basename "$file")"
done

echo "Files in $directory_name renamed with prefix $file_prefix"
