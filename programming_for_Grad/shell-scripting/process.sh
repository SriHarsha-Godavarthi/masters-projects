# the below line indicateds that the below line should execute with bash shell
#!/bin/bash

# Check if directory path is provided as an argument
if [ $# -eq 0 ]; then
    # $# will store no of command line arguments passed
    # $0 first word of entered command
    echo "execute it: $0 <process_name>"
    # exit the script execution
    exit 1
fi
# assign process name from arguments
process_name=$1
# check if process is running or not cmd > pgrep <process_name> this will give processId
# combine standard output and error with &>/dev/null
if pgrep "$process_name" &>/dev/null; then
    # get cpu,memory usage
    resource_usage=$(ps aux | grep "$process_name" | awk '{print "Memory:", $4, "CPU:", $3}')
    # display cpu,memory usage
    echo "$process_name is running. $resource_usage"
else
    # If not running, start the process and log the event
    echo "Starting $process_name..."
    # start the process using exec <process_nane>
    exec "$process_name"
    echo "$process_name has been started."
fi