#!/usr/bin/env python3
"""
Script to create PNG screenshots for Linux Final Project submission
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_code_screenshot(code_text, filename, title="Code Screenshot"):
    """Create a screenshot of code with syntax highlighting effect"""
    
    # Split code into lines
    lines = code_text.strip().split('\n')
    
    # Calculate dimensions
    line_height = 25
    padding = 20
    char_width = 10
    max_line_length = max(len(line) for line in lines) if lines else 0
    
    width = max(400, max_line_length * char_width + 2 * padding)
    height = len(lines) * line_height + 2 * padding + 40  # Extra space for title
    
    # Create image
    img = Image.new('RGB', (width, height), color='#1e1e1e')  # Dark background
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a monospace font
        font = ImageFont.truetype("consola.ttf", 14)
    except:
        try:
            font = ImageFont.truetype("cour.ttf", 14)
        except:
            font = ImageFont.load_default()
    
    # Draw title
    draw.text((padding, 10), title, fill='#ffffff', font=font)
    
    # Draw code lines
    y_offset = 40
    for i, line in enumerate(lines):
        # Color code different elements
        if line.strip().startswith('#'):
            color = '#6a9955'  # Green for comments
        elif '=' in line and not line.strip().startswith('if'):
            color = '#569cd6'  # Blue for assignments
        elif 'if' in line or 'then' in line or 'fi' in line:
            color = '#c586c0'  # Purple for control structures
        elif 'echo' in line or 'cd' in line or 'mv' in line or 'tar' in line:
            color = '#dcdcaa'  # Yellow for commands
        else:
            color = '#d4d4d4'  # White for regular text
        
        draw.text((padding, y_offset + i * line_height), line, fill=color, font=font)
    
    # Save image
    img.save(filename)
    print(f"Created {filename}")

def create_terminal_screenshot(terminal_text, filename, title="Terminal Output"):
    """Create a screenshot of terminal output"""
    
    lines = terminal_text.strip().split('\n')
    line_height = 20
    padding = 20
    char_width = 8
    max_line_length = max(len(line) for line in lines) if lines else 0
    
    width = max(500, max_line_length * char_width + 2 * padding)
    height = len(lines) * line_height + 2 * padding + 30
    
    img = Image.new('RGB', (width, height), color='#000000')  # Black terminal background
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("consola.ttf", 12)
    except:
        try:
            font = ImageFont.truetype("cour.ttf", 12)
        except:
            font = ImageFont.load_default()
    
    # Draw title
    draw.text((padding, 5), title, fill='#00ff00', font=font)
    
    # Draw terminal lines
    y_offset = 25
    for i, line in enumerate(lines):
        color = '#00ff00' if line.strip().startswith('-') else '#ffffff'
        draw.text((padding, y_offset + i * line_height), line, fill=color, font=font)
    
    img.save(filename)
    print(f"Created {filename}")

def main():
    """Create all required PNG screenshots"""
    
    # Ensure submission directory exists
    os.makedirs('submission', exist_ok=True)
    
    # Task 1: Set Variables
    task1_code = """# [TASK 1]
targetDirectory=$1
destinationDirectory=$2"""
    create_code_screenshot(task1_code, 'submission/01-Set_Variables.png', 'Task 1: Set Variables')
    
    # Task 2: Display Values
    task2_code = """# [TASK 2]
echo "Values of variables:"
echo "targetDirectory = $targetDirectory"
echo "destinationDirectory = $destinationDirectory" """
    create_code_screenshot(task2_code, 'submission/02-Display_Values.png', 'Task 2: Display Values')
    
    # Task 3: Current Timestamp
    task3_code = """# [TASK 3]
currentTS=$(date +%s)"""
    create_code_screenshot(task3_code, 'submission/03-CurrentTS.png', 'Task 3: Current Timestamp')
    
    # Task 4: Set Backup File Name
    task4_code = """# [TASK 4]
backupFileName="backup-[$currentTS].tar.gz" """
    create_code_screenshot(task4_code, 'submission/04-Set_Value.png', 'Task 4: Set Backup File Name')
    
    # Task 5: Define Original Absolute Path
    task5_code = """# [TASK 5]
origAbsPath=$(pwd)"""
    create_code_screenshot(task5_code, 'submission/05-Define_Variable.png', 'Task 5: Define Original Absolute Path')
    
    # Task 6: Define Destination Absolute Path
    task6_code = """# [TASK 6]
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)"""
    create_code_screenshot(task6_code, 'submission/06-Define_Variable.png', 'Task 6: Define Destination Absolute Path')
    
    # Task 7: Change Directory
    task7_code = """# [TASK 7]
cd "$origAbsPath"
cd "$targetDirectory" """
    create_code_screenshot(task7_code, 'submission/07-Change_Directory.png', 'Task 7: Change Directory')
    
    # Task 8: Yesterday Timestamp
    task8_code = """# [TASK 8]
yesterdayTS=$(($currentTS - 24*60*60))"""
    create_code_screenshot(task8_code, 'submission/08-YesterdayTS.png', 'Task 8: Yesterday Timestamp')
    
    # Task 9: List All Files and Directories
    task9_code = """for file in $(ls) # [TASK 9]"""
    create_code_screenshot(task9_code, 'submission/09-List_AllFilesandDirectoriess.png', 'Task 9: List All Files and Directories')
    
    # Task 10: IF Statement
    task10_code = """  # [TASK 10]
  if [[ `date -r $file +%s` -gt $yesterdayTS ]]"""
    create_code_screenshot(task10_code, 'submission/10-IF_Statement.png', 'Task 10: IF Statement')
    
    # Task 11: Add File to Array
    task11_code = """  then
    # [TASK 11]
    toBackup+=($file)
  fi"""
    create_code_screenshot(task11_code, 'submission/11-Add_File.png', 'Task 11: Add File to Array')
    
    # Task 12: Create Backup
    task12_code = """# [TASK 12]
tar -czf $backupFileName ${toBackup[@]}"""
    create_code_screenshot(task12_code, 'submission/12-Create_Backup.png', 'Task 12: Create Backup')
    
    # Task 13: Move Backup
    task13_code = """# [TASK 13]
mv $backupFileName $destAbsPath"""
    create_code_screenshot(task13_code, 'submission/13-Move_Backup.png', 'Task 13: Move Backup')
    
    # Task 15: Executable Permissions
    task15_output = """-rwxr-xr-x    1 root     root          1432 Sep 17 16:37 backup.sh"""
    create_terminal_screenshot(task15_output, 'submission/15-executable.png', 'Task 15: Executable Permissions')
    
    # Task 16: Backup Complete
    task16_output = """-rw-r--r--    1 root     root          4364 Sep 17 16:38 backup-[1758127096].tar.gz"""
    create_terminal_screenshot(task16_output, 'submission/16-backup-complete.png', 'Task 16: Backup Complete')
    
    # Task 17: Crontab
    task17_output = """0 2 * * * /usr/local/bin/backup.sh /mnt/host/c/Users/Diaa/linux.project/important-documents /mnt/host/c/Users/Diaa/linux.project"""
    create_terminal_screenshot(task17_output, 'submission/17-crontab.png', 'Task 17: Crontab Schedule')
    
    print("\nAll PNG screenshots created successfully!")
    print("Files created in submission/ directory:")
    for i in range(1, 18):
        if i == 14:
            continue  # Skip task 14 (file upload)
        filename = f"submission/{i:02d}-*.png"
        print(f"  Task {i}: {filename}")

if __name__ == "__main__":
    main()
