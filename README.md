# Rambox Upgrade Script

## Overview
This script automates the process of upgrading Rambox on a Debian-based Linux system. It fetches the latest `.deb` package from the [Rambox GitHub repository](https://github.com/ramboxapp/download), terminates any existing Rambox processes, and installs the new version.

## Features
- **Fetch Latest Release**: Retrieves the latest release information from the Rambox GitHub repository.
- **Download `.deb` Package**: Determines the latest `.deb` file from the repository.
- **Terminate Existing Processes**: Identifies and terminates any running Rambox processes to ensure a clean upgrade.
- **Install New Version**: Installs the newly downloaded `.deb` package.

## How It Works
1. **Fetching the Latest Release**: 
   - The script uses the GitHub API to find the latest release of Rambox.
2. **Downloading the `.deb` Package**:
   - It then searches for a `.deb` package in the release's assets and downloads it.
3. **Terminating Existing Processes**:
   - The script locates any running Rambox processes and terminates them to avoid conflicts during installation.
4. **Installing the New Version**:
   - Finally, it uses `dpkg` to install the downloaded `.deb` package.

## Requirements
- Python 3
- `requests` library in Python
- Internet access for downloading the `.deb` package
- Sudo privileges for installing the `.deb` package

## How to Invoke the Script
1. **Ensure Python 3 and `requests` library are installed**:
   - Install Python 3 and `requests` (if not already installed) using `pip3 install requests`.
2. **Download the Script**:
   - Download or create the script `upgrade_rambox.py` on your system.
3. **Make the Script Executable** (optional):
   - Run `chmod +x upgrade_rambox.py` to make it executable.
4. **Run the Script**:
   - Execute the script by running `python3 upgrade_rambox.py` or `./upgrade_rambox.py` if made executable.
5. **Provide Sudo Password**:
   - The script will prompt for your sudo password as it requires administrative privileges to install the package.

## Note
- This script is designed for Debian-based Linux systems.
- Ensure you have permissions to run scripts and install packages on your system.
- The script should be run in a controlled environment first to ensure it functions as expected.
