# 🛠️ Setting Up a Simple and Reproducible Development Environment

## 📝 Overview
A development environment is your workspace for writing and testing code. It includes programming languages, tools, and dependencies needed for your project.

## 🎯 Key Concepts
- **Version Control**: Track code changes and collaborate using Git
- **Virtual Environment**: Isolated workspace for project dependencies
- **Dependency Management**: Record and share project requirements
- **Environment Reproducibility**: Ensure consistent setup across team

## 💻 Essential Steps

### 1. Git Setup and Basic Commands
```bash
# Initialize a new Git repository
git init

# Stage all files for commit
git add .

# Create initial commit with message
git commit -m "Initial commit"
```

### 2. Virtual Environment Setup
```bash
# Create new virtual environment named 'venv'
python -m venv venv

# Activate virtual environment on Windows
venv\Scripts\activate

# Activate virtual environment on macOS/Linux
source venv/bin/activate

# Install project dependencies
pip install <package-name>
```

### 3. Managing Dependencies
```bash
# Export installed packages to requirements.txt
pip freeze > requirements.txt

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 4. Git Ignore Configuration
```plaintext
# Create .gitignore file with following content
venv/
```

## 🔑 Best Practices
- Always use version control for your projects
- Keep virtual environments project-specific
- Document dependencies in requirements.txt
- Share only necessary files through Git
- Consider using Docker for advanced reproducibility

## 🎓 Summary
A reproducible environment ensures consistent development across team members, reducing "works on my machine" issues and improving collaboration efficiency.

