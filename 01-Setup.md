# 🖥️ Visual Studio Code (VS Code) Overview

## 📌 What is VS Code?
Visual Studio Code (VS Code) is a **free code editor** developed by **Microsoft** for Windows, macOS, and Linux. It provides powerful features for **development, debugging, and version control**.

✅ **Key Functions:**
- Code Editing & Debugging
- Extension Marketplace
- Integrated Terminal & Git Support

---

## 🛠️ Installing VS Code

### **1️⃣ Windows Installation**
- Download from [VS Code website](https://code.visualstudio.com/Download).
- Run the `.exe` installer.
- Select options:
  - Add to PATH
  - Register as editor for files

### **2️⃣ macOS Installation**
- Download the macOS zip file.
- Extract and drag VS Code to **Applications** folder.
- Launch from Applications.

### **3️⃣ Linux Installation**
- **Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install software-properties-common apt-transport-https curl
  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-archive-keyring.gpg
  sudo apt update
  sudo apt install code
  ```
- **Fedora**:
  ```bash
  sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
  sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
  sudo dnf check-update
  sudo dnf install code
  ```
- **Arch**:
  ```bash
  yay -S visual-studio-code-bin
  ```

---

## 🔧 Configuration and Setup

### **1️⃣ Essential Extensions**
- **Python** – For Python development.
- **Prettier** – Code formatting.
- **GitLens** – Enhanced Git integration.

### **2️⃣ Git Integration**
- Install Git for your OS.
- Configure user information:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  ```

### **3️⃣ Settings Customization**
- Open Settings with **Ctrl+,** (Windows/Linux) or **Cmd+,** (macOS).
- Customize theme, font size, editor preferences.
- Edit `settings.json` for advanced configuration.

### **4️⃣ Terminal Integration**
- Access terminal with **Ctrl+`** (Windows/Linux) or **Cmd+`** (macOS).
- Run commands without leaving the editor.

---

## 🔍 How VS Code Works

1️⃣ **Open project** → Access files, folders, and workspace.  
2️⃣ **Edit code** → Use intelligent features like IntelliSense.  
3️⃣ **Debug applications** → Set breakpoints and inspect variables.  
4️⃣ **Use extensions** → Enhance functionality for specific languages or tools.

---

## 📚 Summary
Visual Studio Code **simplifies development**, enhances **productivity**, and provides a **customizable environment** across Windows, macOS, and Linux platforms. 🚀