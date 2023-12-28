# the below line indicateds that the below line should execute with bash shell
#!/bin/bash

# Check if username is provided as an argument
if [ $# -eq 0 ]; then
# $# will store no of command line arguments passed
# $0 first word of entered command
    echo "Usage: $0 <username>"
    exit 1
fi
#store the username entered
username=$1

# Check if user exists or not using id <username>
# &/dev/null - combines both standard out and error
if id "$username" &>/dev/null; then
    # Get user information using getent passwd username
    #get certain part of output seperated by delimiter colon
    # cut is used to extract the field mentioned using -f fieldnumber
    users_fullname=$(getent passwd "$username" | cut -d ":" -f 5)
    home=$(getent passwd "$username" | cut -d ":" -f 6)
    typeOfShell=$(getent passwd "$username" | cut -d ":" -f 7)

    # print user information
    echo "User Name: $username"
    echo "Full Name: $users_fullname"
    echo "Home Directory for user: $home"
    echo "Type of shell: $typeOfShell"
else
   # if user doesn't exsist print this
    echo "User $username does not exist."
fi
