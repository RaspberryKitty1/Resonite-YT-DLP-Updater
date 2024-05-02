import os
import subprocess

executablePath = r"C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe"

# Check if the yt-dlp executable exists at the specified path
if os.path.exists(executablePath):
    confirmMsg = f"yt-dlp has been detected in the following location:\n\n{executablePath}\n\nIs this correct?"
    response = input(f"{confirmMsg} (yes/no): ").strip().lower()

    if response == "yes":
        # Run the executable with the "-U" argument
        subprocess.run([executablePath, "-U"], shell=True)

        # Show a message when execution is complete
        resultMsg = "yt-dlp has been updated to the latest version!\n\nYou should now be able to watch YouTube videos normally."
        print(resultMsg)

        # Wait for Enter key to close
        input("Press Enter to exit...")
    else:
        # Show a message if the user entered "no"
        cancelMsg = "Execution cancelled.\n\nPlease navigate to your NEOS installation directory and update yt-dlp manually."
        print(cancelMsg)

        # Wait for Enter key to close
        input("Press Enter to exit...")
else:
    # Show a message if the executable was not found
    errorMsg = f"yt-dlp executable was not found at the specified path:\n\n{executablePath}\n\nPlease ensure the path is correct."
    print(errorMsg)

    # Wait for Enter key to close
    input("Press Enter to exit...")
