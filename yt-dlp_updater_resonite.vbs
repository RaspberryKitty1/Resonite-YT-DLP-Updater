Set WshShell = CreateObject("WScript.Shell")
executablePath = "C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe"

' Check if the yt-dlp executable exists at the specified path
If CreateObject("Scripting.FileSystemObject").FileExists(executablePath) Then
  ' Prompt user to confirm the path is correct
  confirmMsg = "yt-dlp has been detected in the following location:" & vbCrLf & vbCrLf & executablePath & vbCrLf & vbCrLf & "Is this correct?"
  response = MsgBox(confirmMsg, vbQuestion + vbYesNo, "Confirm Path - Resonite yt-dlp updater by Knackrack615 Ported by Raspberrykitty1")

  If response = vbYes Then
    ' Hide window and run executable with "-U" argument
    WshShell.Run """" & executablePath & """ -U", 0, True

    ' Show message box when execution is complete
    resultMsg = "yt-dlp has been updated to the latest version!" & vbCrLf & vbCrLf & "You should now be able to watch YouTube videos normally."
    MsgBox resultMsg, vbInformation, "Update Completed - Resonite yt-dlp updater by Knackrack615 Ported by Raspberrykitty1"
  Else
    ' Show message box if user clicked "No"
    cancelMsg = "Execution cancelled." & vbCrLf & vbCrLf & "Please navigate to your Resonite installation directory and update yt-dlp manually."
    MsgBox cancelMsg, vbInformation, "Cancelled - Resonite yt-dlp updater by Knackrack615 Ported by Raspberrykitty1"
  End If
Else
  ' Show a message box if the executable was not found
  errorMsg = "yt-dlp executable was not found at the specified path:" & vbCrLf & vbCrLf & executablePath & vbCrLf & vbCrLf & "Please ensure the path is correct."
  MsgBox errorMsg, vbExclamation, "Error - Resonite yt-dlp updater by Knackrack615 Ported by Raspberrykitty1"
End If
