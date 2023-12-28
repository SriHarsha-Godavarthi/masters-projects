
## Scripts Description
  the scripting is done using bash

1. **userinfo.sh**: This script displays information about a user, including full name, home directory, and shell type. Provide a username as an argument to get the user information.
    home~$ ./userinfo.sh <username>
    

2. **healthcheck.sh**: This script reports system information such as date and time, system uptime, users logged in, memory usage, and disk usage.

    home~$ ./healthcheck.sh

3. **backupdire.sh**: This script takes a directory path as input, creates a compressed backup with the current date in the filename, and saves it the same location.

    home~$ ./backupdire.sh <directory_path>

4. **rename.sh**: This script renames all files in a given directory by adding a prefix provided as an argument.

    home~$ ./rename.sh <directory> <prefix>

5. **process.sh**: This script monitors a specific process (process name given as an argument). If the process is not running, it starts the process and logs the event. If the process is running, it logs its current memory and CPU usage.

    home~$ ./process.sh <process_name>

## Example Usage

```bash
# Example for userinfo.sh
./userinfo.sh john_doe

# Example for healthcheck.sh
./healthcheck.sh

# Example for backupdir.sh
./backupdire.sh /path/to/directory

# Example for rename.sh
./rename.sh /path/to/directory prefix

# Example for process.sh
./process.sh bash
```
## References

chat gpt
greeks for greeks - https://www.geeksforgeeks.org/linux-commands/
stack overflow
reference from assignment material