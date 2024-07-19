# Photo Copier Script

This Python script copies all photo files from a source directory to a destination directory. It supports common image file extensions such as `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, and `.tiff`.

## How It Works

The script uses the `os` and `shutil` modules to traverse the source directory and copy files. It checks for files with the specified image extensions and copies them to the destination directory, preserving the original file metadata.

## Prerequisites

- Python 3.x
- Basic understanding of how to run Python scripts

## Script Code

```python
import os
import shutil
