<div align="center">
  
# 🚀 VFY - Verify Your Code

<img src="https://img.shields.io/badge/language-C-blue.svg" alt="Language C">
<img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey.svg" alt="Platform">
<img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License MIT">
<img src="https://img.shields.io/badge/version-1.0.0-orange.svg" alt="Version">

**A modern CLI tool for practicing C programming exercises with automatic verification.**

![Terminal Demo](https://github.com/mgrl39/vfy/raw/assets/demo.gif)

</div>

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🛠️ Installation](#️-installation)
  - [Using pip (recommended)](#using-pip-recommended)
  - [Single-user installation](#single-user-installation)
  - [System-wide installation](#system-wide-installation)
- [📝 Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [🧩 Creating Exercises](#-creating-exercises)
- [🔄 Examples](#-examples)
- [🗑️ Uninstallation](#️-uninstallation)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🌟 Features

VFY (Verify Your Code) is designed to make learning C programming more fun and effective with:

- **📚 Structured Learning Path** - Exercises organized by skill levels (0-7)
- **✅ Automatic Verification** - Instant feedback on your solutions
- **📋 Code Templates** - Quick start with helpful boilerplate code
- **🎨 Beautiful Interface** - Colorful and user-friendly terminal UI
- **🛠️ Customizable Settings** - Configure directories, editor, and more
- **🧩 Exercise Creation** - Create and share your own programming challenges

## 🛠️ Installation

### Using pip (recommended)

The easiest way to install VFY:

```bash
# Install directly from GitHub
pip install git+https://github.com/mgrl39/vfy.git

# Or from local directory
git clone https://github.com/mgrl39/vfy.git
cd vfy
pip install -e .
```

### Single-user installation

```bash
# Clone the repository
git clone https://github.com/mgrl39/vfy.git
cd vfy

# Install for current user (no sudo required)
make user-install

# Add to PATH (add this line to your .bashrc or .zshrc)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### System-wide installation

```bash
# Clone the repository
git clone https://github.com/mgrl39/vfy.git
cd vfy

# Install system-wide (requires sudo)
sudo make install
```

## 📝 Usage

VFY provides an intuitive command-line interface:

| Command | Description |
|---------|-------------|
| `vfy help` | Show all available commands |
| `vfy list` | List all available exercise levels |
| `vfy list <level>` | List exercises in a specific level |
| `vfy get <level>` | Get a random exercise from a level |
| `vfy edit` | Open current exercise in your editor |
| `vfy check` | Verify your solution against expected output |
| `vfy status` | Show current exercise status |
| `vfy config` | Show or modify configuration options |
| `vfy create` | Create a new exercise |

## ⚙️ Configuration

Customize VFY to fit your preferences:

```bash
# View current configuration
vfy config

# Change exercise directory
vfy config exercises_dir ~/my_exercises

# Change default editor
vfy config editor nano

# Toggle auto-open editor feature
vfy config auto_open_editor false

# Add compiler flags
vfy config compiler_flags "-Wall -Wextra -Werror"
```

You can also use environment variables:

```bash
# Define exercise location
export VFY_EXERCISES_DIR=~/my_exercises

# Define subject location
export VFY_SUBJECTS_DIR=~/my_exercise_subjects

# Define compiler
export CC=gcc
```

## 🧩 Creating Exercises

Create your own exercises to practice or share with others:

```bash
# Interactive exercise creation
vfy create
```

Or create exercises manually:

1. Create a directory at `~/.vfy/subjects/level_X/exercise_name`
2. Add the following files:
   - `subject.txt`: Exercise description
   - `expected_output.txt`: Expected program output
   - `template.c`: Template code for users

## 🔄 Examples

Here's how a typical workflow looks:

```bash
# Get a random exercise from level 1
vfy get 1

# The exercise details will be displayed
# A working directory is created with a template

# Open the exercise in your editor
vfy edit

# After coding your solution
vfy check

# If correct, you'll see:
# ✅ Your solution is correct!

# If not, you'll see:
# ❌ Output doesn't match expected result.
# With a detailed diff of what went wrong
```

## 🗑️ Uninstallation

```bash
# Uninstall (with sudo if you used system installation)
sudo make uninstall
```

## 🤝 Contributing

We welcome contributions to make VFY better:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  
**Created with ❤️ for C programming enthusiasts**

<a href="https://github.com/mgrl39/vfy/issues">Report Bug</a> · 
<a href="https://github.com/mgrl39/vfy/issues">Request Feature</a>

</div> 