# 🖥️ Complete VS Code & Python Installation Guide

## 📌 Overview
This guide provides step-by-step instructions for installing **Visual Studio Code** and **Python** on the three major operating systems: **Windows**, **macOS**, and **Linux**. Both tools are essential for modern software development.

✅ **What You'll Install:**
- Visual Studio Code (VS Code) - A powerful code editor
- Python - A versatile programming language
- Python extensions for VS Code

---

## 🪟 Windows Installation

### **1️⃣ Installing VS Code on Windows**
- **Download VS Code**:
  - Visit the [Visual Studio Code website](https://code.visualstudio.com/download)
  - Click the **Windows** download button
  - The `.exe` installer will download automatically

- **Run the Installer**:
  - Open the downloaded `.exe` file
  - Accept the license agreement
  - Select destination location (or keep default)
  - Important: Check these options:
    - ✓ Create a desktop icon
    - ✓ Add to PATH
    - ✓ Register Code as an editor for supported file types
  - Click **Install** and wait for completion
  - Launch VS Code when finished

### **2️⃣ Installing Python on Windows**
- **Download Python**:
  - Visit the [Python downloads page](https://www.python.org/downloads/)
  - Click **Download Python** (latest version)
  
- **Run the Installer**:
  - Open the downloaded `.exe` file
  - **IMPORTANT**: Check ✓ **Add Python to PATH**
  - Select **Install Now** (recommended)
  - Wait for installation to complete
  
- **Verify Installation**:
  - Open Command Prompt (Win+R, type `cmd`, press Enter)
  - Type `python --version` and press Enter
  - You should see the Python version number

### **3️⃣ Setting Up Python in VS Code (Windows)**
- Open VS Code
- Click on the **Extensions** icon in the sidebar (or press Ctrl+Shift+X)
- Search for "**Python**" (by Microsoft)
- Click **Install**
- Create a new file with `.py` extension
- VS Code will recommend Python interpreter - select the one you installed

---

## 🍎 macOS Installation

### **1️⃣ Installing VS Code on macOS**
- **Download VS Code**:
  - Visit the [Visual Studio Code website](https://code.visualstudio.com/download)
  - Click the **macOS** download button
  - A `.zip` file will download
  
- **Install VS Code**:
  - Open the downloaded `.zip` file
  - Drag **Visual Studio Code.app** to your **Applications** folder
  - Open VS Code from Applications
  - (Optional) Add VS Code to Dock by right-clicking the icon and selecting **Options → Keep in Dock**

### **2️⃣ Installing Python on macOS**
- **Download Python**:
  - Visit the [Python downloads page](https://www.python.org/downloads/)
  - Click **Download Python** (latest version)
  - A `.pkg` installer will download
  
- **Run the Installer**:
  - Open the downloaded `.pkg` file
  - Follow the installation steps
  - The installer will place Python in `/Applications/Python`
  
- **Verify Installation**:
  - Open Terminal (Applications → Utilities → Terminal)
  - Type `python3 --version` and press Enter
  - You should see the Python version number

- **Alternative Installation via Homebrew**:
  - If you have Homebrew installed, you can run:
  ```bash
  brew install python
  ```

### **3️⃣ Setting Up Python in VS Code (macOS)**
- Open VS Code
- Click on the **Extensions** icon in the sidebar (or press Cmd+Shift+X)
- Search for "**Python**" (by Microsoft)
- Click **Install**
- Create a new file with `.py` extension
- VS Code will recommend Python interpreter - select the one you installed

---

## 🐧 Linux Installation

### **1️⃣ Installing VS Code on Linux**
- **Ubuntu/Debian-based Distributions**:
  ```bash
  # Update package information
  sudo apt update
  # Install dependencies
  sudo apt install software-properties-common apt-transport-https wget
  # Import Microsoft GPG key
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
  sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
  sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
  rm -f packages.microsoft.gpg
  # Install VS Code
  sudo apt update
  sudo apt install code
  ```

- **Fedora/RHEL-based Distributions**:
  ```bash
  # Import Microsoft GPG key
  sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
  # Add VS Code repository
  sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
  # Install VS Code
  sudo dnf check-update
  sudo dnf install code
  ```

- **Arch Linux**:
  ```bash
  # Install from AUR
  yay -S visual-studio-code-bin
  # or
  paru -S visual-studio-code-bin
  ```

### **2️⃣ Installing Python on Linux**
- **Ubuntu/Debian-based Distributions**:
  ```bash
  # Update package information
  sudo apt update
  # Install Python
  sudo apt install python3 python3-pip python3-venv
  ```

- **Fedora/RHEL-based Distributions**:
  ```bash
  sudo dnf install python3 python3-pip
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -S python python-pip
  ```

- **Verify Installation**:
  ```bash
  python3 --version
  pip3 --version
  ```

### **3️⃣ Setting Up Python in VS Code (Linux)**
- Open VS Code
- Click on the **Extensions** icon in the sidebar (or press Ctrl+Shift+X)
- Search for "**Python**" (by Microsoft)
- Click **Install**
- Create a new file with `.py` extension
- VS Code will recommend Python interpreter - select the one you installed

---

## 🚀 Testing Your Installation

### **1️⃣ Create a Simple Python Project**
1. Open VS Code
2. Create a new file: `File → New File` (or Ctrl+N / Cmd+N)
3. Save it as `hello.py`: `File → Save` (or Ctrl+S / Cmd+S)
4. Write this code:
   ```python
   print("Hello, World!")
   print("Python and VS Code are now installed!")
   ```
5. Run the code:
   - Click the "Play" button in the top-right corner, or
   - Right-click and select "Run Python File in Terminal", or
   - Press F5

### **2️⃣ Verify Python Extensions**
1. Your VS Code should provide:
   - Syntax highlighting for Python
   - Code completion suggestions
   - Error and warning indicators
   - Option to select Python interpreter

---

## 📚 Summary
Congratulations! You've successfully installed **Visual Studio Code** and **Python** on your operating system. These tools provide a powerful environment for Python development, with features like syntax highlighting, code completion, debugging, and more. 

Both VS Code and Python are cross-platform, meaning the skills you learn will transfer across Windows, macOS, and Linux environments. Happy coding! 🚀
