import os
import tkinter as tk
from tkinter import messagebox
import subprocess

executablePath = r"C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe"

# Check if the yt-dlp executable exists at the specified path
if os.path.exists(executablePath):
    # Create a Tkinter window to display a confirmation message
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    confirmMsg = f"yt-dlp has been detected in the following location:\n\n{executablePath}\n\nIs this correct?"
    response = messagebox.askyesno("Confirm Path - Resonite yt-dlp updater by Knackrack615 Ported by raspberrykitty1", confirmMsg)

    if response:
        # Run the executable with the "-U" argument
        subprocess.run([executablePath, "-U"], shell=True)

        # Show a message box when execution is complete
        resultMsg = "yt-dlp has been updated to the latest version!\n\nYou should now be able to watch YouTube videos normally."
        messagebox.showinfo("Update Completed - Resonite yt-dlp updater by Knackrack615 Ported by raspberrykitty1", resultMsg)
    else:
        # Show a message box if the user clicked "No"
        cancelMsg = "Execution cancelled.\n\nPlease navigate to your Resonite installation directory and update yt-dlp manually."
        messagebox.showinfo("Cancelled - Resonite yt-dlp updater by Knackrack615 Ported by raspberrykitty1", cancelMsg)
else:
    # Show a message box if the executable was not found
    errorMsg = f"yt-dlp executable was not found at the specified path:\n\n{executablePath}\n\nPlease ensure the path is correct."
    messagebox.showerror("Error - Resonite yt-dlp updater by Knackrack615 Ported by raspberrykitty1", errorMsg)
