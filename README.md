<div align="center">
  
# 🚀 VFY - Verify Your Code

<img src="https://img.shields.io/badge/language-C-blue.svg" alt="Language C">
<img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey.svg" alt="Platform">
<img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License MIT">
<img src="https://img.shields.io/badge/version-1.0.0-orange.svg" alt="Version">

**A tool for practicing C programming exercises with automatic verification.**

</div>

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🛠️ Installation](#️-installation)
- [📝 Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [🧩 Creating Exercises](#-creating-exercises)
- [🔄 Examples](#-examples)
- [🗑️ Uninstallation](#️-uninstallation)

---

## 🌟 Features

VFY (Verify Your Code) is designed to make learning C programming more fun and effective with:

- **📚 Structured Learning** - Exercises organized by skill levels
- **✅ Automatic Verification** - Instant feedback on your solutions
- **📋 Code Templates** - Quick start with helpful boilerplate code
- **🎨 Attractive Interface** - Colorful and user-friendly terminal UI

## 🛠️ Installation

Installation is very simple:

```bash
# Clone the repository
git clone https://github.com/mgrl39/vfy.git
cd vfy

# Install (requires sudo)
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

## ⚙️ Configuration

You can use environment variables to customize VFY:

```bash
# Define exercises location
export VFY_EXERCISES_DIR=~/my_exercises

# Define subjects location
export VFY_SUBJECTS_DIR=~/my_subjects

# Define compiler
export CC=gcc
```

## 🧩 Creating Exercises

You can create exercises manually:

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
# Uninstall (requires sudo)
sudo make uninstall
```

---

<div align="center">
  
**Created for C programming enthusiasts**

</div> 