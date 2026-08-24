# Downloads Manager

A lightweight, robust, object-oriented Python utility designed to automatically organize and triage files in your system's `Downloads` folder into categorized subdirectories based on file extensions.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
  - [Command Line Interface (CLI)](#command-line-interface-cli)
  - [Programmatic Usage](#programmatic-usage)
- [Configuration](#configuration)
- [Error Handling & Edge Cases](#error-handling--edge-cases)

---

## Overview

The **Downloads Manager** scans your Downloads folder, identifies file types according to configurable extension mapping rules, and safely moves each file into its corresponding category folder (e.g., `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Executables`, `Others`).

Built strictly with Python's standard library (`pathlib`, `shutil`, `os`), it requires zero external dependencies, making it portable and lightweight across Windows, macOS, and Linux.

---

## Key Features

- **Automated Categorization**: Maps file extensions to targeted folders dynamically.
- **Zero External Dependencies**: Uses native Python standard library tools (`pathlib.Path`, `shutil`).
- **Cross-Platform Compatibility**: Resolves OS-specific home and download paths reliably.
- **Robust Exception Handling**: Prevents pipeline interruption on file lock, permission denial, or collision errors.
- **Extensible Architecture**: Class-based modular design (`DownloadsOrganizer`) allowing effortless integration into background daemons, cron jobs, or task schedulers.

---

## Architecture & Design Decisions

### 1. Object-Oriented Design (`DownloadsOrganizer`)
The core functionality is encapsulated within the `DownloadsOrganizer` class in `main.py`. This decoupling ensures:
- Easy unit testing and mocking.
- Ability to pass custom download targets or custom extension mappings.
- Clean separation of concerns between path discovery, directory provisioning, file scanning, categorization, and file moving.

### 2. Path Abstraction with `pathlib.Path`
Rather than relying on raw string manipulation, the codebase utilizes `pathlib.Path` objects to ensure platform-agnostic file path operations (handling both Windows `\` and POSIX `/` separators seamlessly).

---

## Project Structure

```text
downloadsManager/
├── main.py          # Primary entry point & DownloadsOrganizer class definition
└── README.md        # Technical project documentation
```

---

## Prerequisites

- **Python**: Python 3.10 or higher recommended.
- **Dependencies**: None (Standard Library only).

---

## Installation & Setup

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/downloadsManager.git
   cd downloadsManager
   ```

2. **Verify Python Installation**:
   ```bash
   python --version
   ```

---

## Usage

### Command Line Interface (CLI)

Run the script directly from your terminal:

```bash
python main.py
```

**Output**:
```text
Downloads Manager completed organization.
```

### Programmatic Usage

You can import and use the `DownloadsOrganizer` class directly within your Python scripts or automation workflows:

```python
from pathlib import Path
from main import DownloadsOrganizer

# Instantiate using default user Downloads directory
organizer = DownloadsOrganizer()
organizer.organize_downloads()

# Or instantiate targeting a custom folder directory
custom_organizer = DownloadsOrganizer(download_dir="/path/to/custom/folder")
custom_organizer.organize_downloads()
```

---

## Configuration

Category mappings are defined in the `CATEGORY_MAPPINGS` class attribute in `main.py`:

```python
CATEGORY_MAPPINGS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Others": []
}
```

To add new categories or extensions, update the dictionary keys and extension lists accordingly.

---

## Error Handling & Edge Cases

- **Missing Directories**: `create_category_directories()` automatically provisions missing destination folders prior to moving files.
- **Hidden / Dot Files**: `scan_downloads_folder()` ignores hidden files (starting with `.`) to prevent moving system metadata or configuration files (e.g., `.DS_Store`, `.gitignore`).
- **File Collisions & System Lock**: `move_file_to_category()` catches `FileExistsError` and `OSError` exceptions to ensure one failing file move operation does not crash the organizing loop.

---



.
