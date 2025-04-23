# 🖥️ Complete Guide to Setting Up Your Programming Environment

## 📌 What is This Guide?
This guide covers the **complete setup process** for the **TCM Programming 100 course**. It walks through installing essential tools like **VS Code**, **Git**, **GitHub**, and **Python virtual environments**.

✅ **Key Components:**
- VS Code Installation & Configuration
- Git Setup & GitHub Integration
- Python Environment Management
- Project Organization

---

## 🛠️ Installing and Configuring Tools

### **1️⃣ Visual Studio Code (VS Code)**
- **Windows**: Download from [VS Code website](https://code.visualstudio.com/) and run installer.
- **macOS**: Download and drag VS Code to Applications folder.
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install software-properties-common apt-transport-https wget
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
  sudo apt update
  sudo apt install code
  ```

### **2️⃣ VS Code Configuration**
- Change theme: Press **Ctrl+Shift+P** (or **Cmd+Shift+P**) and search for "Color Theme"
- Adjust font size: Open Settings (**Ctrl+,** or **Cmd+,**) and search for "Font Size"
- Install extensions:
  - **Python**
  - **Prettier - Code Formatter**
  - **GitLens**

### **3️⃣ Git Installation**
- **Windows**: Download from [Git website](https://git-scm.com/)
- **macOS**: Use pre-installed Git or install via `brew install git`
- **Linux**: Install with `sudo apt install git`
- Verify with `git --version`

### **4️⃣ Git Configuration**
- Set name and email:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

---

## 🌐 GitHub Setup

### **1️⃣ Account Creation**
- Visit [GitHub](https://github.com) and sign up for an account.
- Verify your email address.

### **2️⃣ Repository Creation**
- Click the "+" icon and select "New repository".
- Name your repository (e.g., "Programming-100-Notes").
- Click "Create repository".

### **3️⃣ GitHub Authentication Methods**

#### **Option A: Using GitHub CLI (gh) - Recommended for Beginners**
GitHub CLI provides a much simpler authentication process:

1. **Install GitHub CLI**:
   - **Windows**: `winget install --id GitHub.cli`
   - **macOS**: `brew install gh`
   - **Linux**: 
     ```bash
     curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
     echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
     sudo apt update
     sudo apt install gh
     ```

2. **Authenticate with GitHub**:
   ```bash
   gh auth login
   ```
   - Select "GitHub.com"
   - Select "HTTPS" 
   - Confirm to authenticate with your GitHub credentials
   - Choose browser authentication when prompted
   - Complete the authentication in the browser window that opens

3. **Verify authentication**:
   ```bash
   gh auth status
   ```

This method eliminates the need for manual SSH setup and will handle authentication for git commands automatically.

#### **Option B: SSH Setup (Alternative Method)**
- Generate SSH keys:
  ```bash
  ssh-keygen -t rsa -b 4096 -C "you@example.com"
  ```
- Copy your public key:
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```
- Add to GitHub: Settings → SSH and GPG keys → New SSH key
- Test with: `ssh -T git@github.com`

---

## 📂 Python Project Setup

### **1️⃣ Project Creation**
- Create project folder:
  ```bash
  mkdir Programming-100-Notes
  cd Programming-100-Notes
  ```
- Create a Python file:
  ```bash
  touch main.py
  code main.py
  ```
- Test with: `print("Hello, World!")`

### **2️⃣ Virtual Environment**
- Create environment:
  ```bash
  python3 -m venv venv
  ```
- Activate:
  - **Windows**: `.\venv\Scripts\activate`
  - **macOS/Linux**: `source venv/bin/activate`
- Install packages: `pip install flask`
- Deactivate: `deactivate`

---

## 🔍 GitHub Integration

1️⃣ **Initialize repository**: `git init`  
2️⃣ **Add files**: `git add .`  
3️⃣ **Commit changes**: `git commit -m "Initial commit"`  
4️⃣ **Push to GitHub**:

**If using GitHub CLI (gh)**:
```bash
# Create a repository on GitHub and push your code
gh repo create Programming-100-Notes --private --source=. --remote=origin
git push -u origin main
```

**If using traditional method**:
```bash
git remote add origin git@github.com:YourUsername/Programming-100-Notes.git
git push -u origin main
```

---

## 📚 Summary
This guide provides a **complete development environment** for the TCM Programming 100 course. With VS Code, Git, GitHub, and Python virtual environments properly configured, you're ready to **begin coding** efficiently and effectively. Using GitHub CLI (gh) makes authentication much simpler, especially for beginners. 🚀