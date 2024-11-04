# AutoFileOrganizer

**AutoFileOrganizer** is a Python script that organizes files within a directory by categorizing them into folders based on file type. It's designed to keep your files organized and make it easy to locate various types of files, from images and documents to videos and archives.

## Key Features
- Organizes files into folders like **Images**, **Documents**, **Videos**, **Music**, and **Archives** based on file extensions.
- Automatically creates folders if they don’t exist.
- Moves files with unrecognized extensions into an **Other** folder.
- Handles files without extensions by placing them in the **Other** folder.
- Simple to use and easy to customize.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/AutoFileOrganizer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AutoFileOrganizer
    ```

### Usage
1. Place the script in the directory you want to organize, or specify the target directory.
2. Run the script:
    ```bash
    python auto-file-organizer.py
    ```

The script will create folders as needed and move files based on their file type.

### File Categories
The script currently organizes files into these categories:
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Videos**: `.mp4`, `.mov`, `.avi`
- **Music**: `.mp3`, `.wav`
- **Archives**: `.zip`, `.tar`, `.rar`
- **Other**: For unrecognized or extension-less files

### Customization
You can easily customize the `fileFormat` dictionary in the script to add or modify file categories.

## Example Output
