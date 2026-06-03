Local File Management System
A simple, interactive Command-Line Interface (CLI) application built in Python for managing local files and directories. The system provides a wrapper around native system calls, allowing users to perform standard CRUD (Create, Read, Update, Delete) operations on files dynamically and safely.

✨ Features
📊 Directory Auditing: Automatically lists all existing files and subdirectories with numerical indexing before every operation.

📝 Safe File Creation: Prevents accidental overwrites by checking if a filename already exists before writing new data.

📖 Instant File Reading: Validates paths to ensure you are targetting a readable file and outputs text contents directly to the terminal.

🔄 Granular File Updates: Provides a detailed sub-menu supporting three distinct operations:

Rename: Shifts the absolute path and updates the filename.

Overwrite: Wipes existing text and replaces it with new user input.

Append: Appends new lines of text smoothly to the end of the file.

🗑️ Secure Removal: Verifies physical path existence before calling operational system hooks to delete target files.

🛡️ Graceful Error Handling: Completely wrapped inside try-except blocks to prevent system crashes from invalid user inputs or missing permissions.

🛠️ System Architecture & Methods
The application divides its core responsibilities across clean, dedicated utility functions:

Method Name	Core Functionality	Modules Used
readfileandfolder()	Performs a deep recursive scan (rglob('*')) to list files and directories.	pathlib.Path
createfile()	Checks for duplicate names and creates a new file in write (w) mode.	pathlib.Path, open()
readfile()	Ensures the target is an actual file (not a folder) and opens it in read (r) mode.	pathlib.Path, open()
updatefile()	Hosts a secondary sub-menu allowing users to choose between renaming, overwriting, or appending (a).	pathlib.Path, open()
deletefile()	Contacts lower-level OS hooks to permanently wipe the targeted file.	pathlib.Path, os
🚀 How to Run the Application
Prerequisites
Make sure you have Python 3.x installed on your operating system.

Steps to Execute
Clone the repository or download the main.py file:

Bash
git clone https://github.com/YOUR_USERNAME/bank_management.git
cd bank_management
Run the script directly from your terminal:

Bash
python main.py
🎮 User Interface Flow
When launched, the program displays a primary interactive menu prompt:

Plaintext
press 1 for creating a file 
press 2 for reading a file 
press 3 for updating a file 
press 4 for deleting a file 
plzz tell your response:-
Once an option is chosen, the application lists the contents of your folder to help you pick the right file, processes your commands, and prints status confirmations (e.g., "file created successfully").
