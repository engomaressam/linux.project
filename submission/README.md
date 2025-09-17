# Linux Commands and Shell Scripting - Final Project Submission

## Project Overview
This project implements a scheduled backup script (`backup.sh`) that automatically backs up encrypted password files that have been updated within the past 24 hours.

## Files Submitted

### Script File
- `backup.sh` - The completed backup script

### Screenshots (Code Sections)
- `task1_code.txt` - Task 1: Set Variables
- `task2_code.txt` - Task 2: Display Values  
- `task3_code.txt` - Task 3: Current Timestamp
- `task4_code.txt` - Task 4: Set Backup File Name
- `task5_code.txt` - Task 5: Define Original Absolute Path
- `task6_code.txt` - Task 6: Define Destination Absolute Path
- `task7_code.txt` - Task 7: Change Directory
- `task8_code.txt` - Task 8: Yesterday Timestamp
- `task9_code.txt` - Task 9: List All Files and Directories
- `task10_code.txt` - Task 10: IF Statement for File Check
- `task11_code.txt` - Task 11: Add File to Backup Array
- `task12_code.txt` - Task 12: Create Backup
- `task13_code.txt` - Task 13: Move Backup File

### Screenshots (Execution Results)
- `task15_executable.txt` - Task 15: Executable Permissions
- `task16_backup_complete.txt` - Task 16: Backup File Created
- `task17_crontab.txt` - Task 17: Crontab Schedule

## Script Features
- Validates command line arguments
- Creates timestamped backup files
- Finds files modified in the last 24 hours
- Compresses and archives files using tar
- Moves backup to destination directory
- Scheduled to run daily at 2 AM

## Testing
The script was successfully tested with the provided `important-documents` folder and created a backup file `backup-[1758127096].tar.gz`.

## Cron Job
The script is scheduled to run every day at 2 AM:
```
0 2 * * * /usr/local/bin/backup.sh /mnt/host/c/Users/Diaa/linux.project/important-documents /mnt/host/c/Users/Diaa/linux.project
```
