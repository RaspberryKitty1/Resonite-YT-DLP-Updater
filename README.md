

# Resonite-YT-DLP-Updater

A script to update yt-dlp.exe in your Resonite install directory.

Original script by Knackrack615 for NeosVR.

Ported by Raspberrykitty1.

Although Resonite is usually kept up-to-date, these scripts are here in case of significant updates to yt-dlp while waiting for a Resonite update.
The original script was only a .vbs file.

I have ported the original script and also converted it into Python, JavaScript, and VBScript for more versatility.

How to Use:

## Prerequisites:

Ensure that yt-dlp.exe is located in the Resonite installation directory at C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe. If it's located elsewhere, update the paths in the scripts accordingly.

## Running the Scripts:

You have several options for updating yt-dlp using different scripts:

1. JavaScript (yt-dlp-updater.js)

Requirements: Node.js installed on your system.

How to run:

Open a terminal or command prompt.

Navigate to the directory where the yt-dlp-updater.js script is located.

Run the command:

```node yt-dlp-updater.js```

Follow the prompts in the terminal. You will be asked if the detected path is correct. If confirmed, the script will update yt-dlp.



2. VBScript (yt-dlp-updater.vbs)

Requirements: Windows Script Host (WSH) (default on Windows).

How to run:

Double-click the yt-dlp-updater.vbs file.

A prompt will appear asking you to confirm the path of yt-dlp.exe. If correct, it will update the executable automatically.



3. Python (yt-dlp-updater.py)

Requirements: Python installed on your system along with TK. 

How to run:

Open a terminal or command prompt.

Navigate to the directory where the yt-dlp-updater.py script is located.

Run the command:

```python yt-dlp-updater.py```

A Tkinter window will appear asking if the path is correct. Confirm and the script will update yt-dlp.

4. Python (No Tkinter Required) (yt-dlp-updater(NoTK required).py)

Requirements: Python installed on your system.

How to run:

Open a terminal or command prompt.

Navigate to the directory where the yt-dlp-updater(NoTK required).py script is located.

Run the command:

```python yt-dlp-updater(NoTK required).py```

This version does not require Tkinter and will prompt you via the command line for confirmation to update yt-dlp.

## Troubleshooting:

yt-dlp Not Found:
If you get an error that yt-dlp.exe is not found, double-check that it is located in the correct directory:

`C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe`

If it's located elsewhere, you will need to update the path in the script.

Script Execution Issues:
Make sure you have the required software (`Node.js`, `Python`, or Windows Script Host) installed on your system, depending on which script you are running.


## Notes:

These scripts are mainly for use with Resonite, but they should work with other installations of yt-dlp as well, provided the correct executable path is set.

The scripts perform the update by running yt-dlp.exe -U, which checks for and installs updates to yt-dlp.

## Disclaimer:

This project is not affiliated with or endorsed by Yellow Dog Man Studios or Resonite. The scripts are provided as-is for personal use to clean up cache files from the game Resonite.
