ZipCracker

ZipCracker is a command-line tool designed to brute-force password-protected ZIP files using a provided list of passwords. The tool attempts to extract the contents of the ZIP file using each password in the list until the correct password is found or the list is exhausted.
Usage Instructions
1. Installation

    Ensure Python is installed on your system. You can download it from python.org.
    Download the ZipCracker script.

2. Installing Dependencies

Run the following command in the terminal to install the required dependencies:

bash

pip install zipfile

3. Usage

    Open a terminal window.
    Navigate to the directory containing the ZipCracker script.

Run the script using the following command:

bash

python ZipCracker.py PASSWORD_FILE ZIP_FILE

Replace PASSWORD_FILE with the path to a file containing a list of passwords (one per line) and ZIP_FILE with the path to the target password-protected ZIP file.

Example:

bash

python ZipCracker.py common-passwords.txt example.zip

4. Output

    The tool will display progress, indicating the number of attempts made to crack the password.
    If successful, it will print the password and the line number from the password list where the match was found.
    If unsuccessful, it will inform you that the password was not found.

Notes

    Ensure that you have the necessary permissions to install Python packages and access the specified files.
    Use this tool responsibly and only on files for which you have the legal right to access the contents.
