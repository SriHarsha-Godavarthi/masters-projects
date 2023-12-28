# the below line indicateds that the below line should execute with bash shell
#!/bin/bash

# Display system information
echo "Date and Time: $(date)"  # gives current date and time
echo "System Uptime: $(uptime)" # system uptime
echo "Logged In Users: $(who | wc -l)" # no of user logged in
# who will give users loggedin
# wc -l will count no of output lines (.i.e users) 
echo "Memory Usage: $(free -h | grep Mem)"
#gets memory usage information using the free  
# extract the line containing "Mem" using grep which gives memory info
echo "Disk Usage: $(df -h)"
# gets disk usage information
