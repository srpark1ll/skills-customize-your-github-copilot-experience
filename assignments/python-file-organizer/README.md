# 📘 Assignment: Python File Organizer

## 🎯 Objective

Build a command-line tool that organizes files into folders based on their file types. Use Python's `pathlib` and `shutil` to inspect paths and move files safely, with a preview mode before any changes are made.

## 📝 Tasks

### 🛠️ Classify Files and Preview Changes

#### Description
Write functions that classify files by their extensions and create a plan for organizing the files in a folder. The program should show the planned changes without modifying files by default.

#### Requirements
Completed program should:

- Use `pathlib.Path` to inspect a user-provided folder and its files
- Classify file extensions case-insensitively into `images`, `documents`, `spreadsheets`, or `other`
- Print each source and planned destination path without moving files in preview mode
- Skip subfolders when building the plan


### 🛠️ Apply the File Organization Safely

#### Description
Add command-line options to apply the plan, create destination folders as needed, and move files with `shutil`. Keep preview mode as the default so a student must explicitly request changes.

#### Requirements
Completed program should:

- Accept a folder path and an optional `--apply` flag using `argparse`
- Move files only when `--apply` is provided
- Create category folders only when applying the plan
- Skip and report a file if a file with the same name already exists at its destination; never overwrite it
- Display a clear error when the supplied path is not a folder


### 🛠️ Test the Organizer

#### Description
Use temporary folders to check the organizer's behavior without changing personal files. Include files with different extensions and a destination-name conflict.

#### Requirements
Completed program should:

- Use Python's `unittest` and `tempfile` modules to test file classification and move planning
- Verify preview mode leaves the original files in place
- Verify apply mode moves files to the expected category folders
- Verify a name conflict is reported and the existing destination file is unchanged