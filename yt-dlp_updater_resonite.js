const { exec } = require('child_process');
const path = require('path');
const os = require('os');

const executablePath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Resonite\\RuntimeData\\yt-dlp.exe";
const userProfile = os.homedir();

function fileExists(filePath) {
  const fs = require('fs');
  return fs.existsSync(filePath);
}

if (fileExists(executablePath)) {
  const confirmMsg = `yt-dlp has been detected in the following location:\n\n${executablePath}\n\nIs this correct?`;

  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  readline.question(confirmMsg, (response) => {
    if (response.toLowerCase() === 'yes' || response.toLowerCase() === 'y') {
      const command = `"${executablePath}" -U`;
      exec(command, (error, stdout, stderr) => {
        if (error) {
          console.error(`Error: ${error}`);
        } else {
          const resultMsg = "yt-dlp has been updated to the latest version!\n\nYou should now be able to watch YouTube videos normally.";
          console.log(resultMsg);
        }
      });
    } else {
      const cancelMsg = "Execution cancelled.\n\nPlease navigate to your Resonite installation directory and update yt-dlp manually.";
      console.log(cancelMsg);
    }
    readline.close();
  });
} else {
  const errorMsg = `yt-dlp executable was not found at the specified path:\n\n${executablePath}\n\nPlease ensure the path is correct.`;
  console.error(`Error: ${errorMsg}`);
}
