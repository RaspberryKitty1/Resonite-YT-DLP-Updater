# Resonite-YT-DLP-Updater

A collection of scripts to update `yt-dlp.exe` in your **Resonite** installation directory.

- **Original Script by**: [Knackrack615](https://github.com/Knackrack615) (for NeosVR)  
- **Ported and Expanded by**: [Raspberrykitty1](https://github.com/Raspberrykitty1)

Although Resonite typically includes a bundled version of `yt-dlp`, these scripts are useful for updating it manually—especially when significant updates occur before an official Resonite patch is released.

---

## 📁 Prerequisites

Ensure `yt-dlp.exe` is located at the default Resonite path:

```
C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe
```

If your installation differs, update the executable path in the script(s) accordingly.

---

## ▶️ How to Use

You can use any of the following scripts, depending on your environment and preference:

---

### 1. **JavaScript** (`yt-dlp-updater.js`)

- **Requirements**: [Node.js](https://nodejs.org/) installed.

**How to run**:

```bash
# In terminal or command prompt
node yt-dlp-updater.js
```

- The script will detect the path and ask for confirmation.
- Upon confirmation, it will run `yt-dlp.exe -U` to update.

---

### 2. **VBScript** (`yt-dlp-updater.vbs`)

- **Requirements**: Windows Script Host (included with Windows).

**How to run**:

- Double-click the `.vbs` file.
- A prompt will appear asking for confirmation of the `yt-dlp.exe` path.
- If correct, it will proceed to update.

---

### 3. **Python with GUI** (`yt-dlp-updater.py`)

- **Requirements**: Python (with Tkinter module installed — included by default in most installations).

**How to run**:

```bash
python yt-dlp-updater.py
```

- A simple Tkinter GUI will prompt you to confirm the executable path.
- Upon confirmation, the update will be performed.

---

### 4. **Python (No GUI)** (`yt-dlp-updater(NoTK required).py`)

- **Requirements**: Python installed (no GUI modules needed).

**How to run**:

```bash
python yt-dlp-updater(NoTK required).py
```

- Command-line-based prompts will guide you through confirming the path and proceeding with the update.

---

## 🛠 Troubleshooting

### 🔍 **yt-dlp.exe Not Found**

- Double-check the default path:

  ```
  C:\Program Files (x86)\Steam\steamapps\common\Resonite\RuntimeData\yt-dlp.exe
  ```

- If different, edit the script to match your actual `yt-dlp.exe` location.

### ⚙️ **Script Not Running**

- Make sure you have the appropriate environment installed:
  - **Node.js** for JavaScript
  - **Python** for `.py` scripts
  - **Windows Script Host** for VBScript (enabled by default)

---

## 📝 Notes

- While designed for **Resonite**, these scripts can be adapted for any `yt-dlp.exe` install—just update the path in the script.
- The core update functionality relies on:

  ```bash
  yt-dlp.exe -U
  ```

---

## ⚠️ Disclaimer

This project is **not affiliated with or endorsed by Yellow Dog Man Studios or Resonite**.  
The scripts are provided **as-is** for personal use to help you keep `yt-dlp.exe` up to date.
