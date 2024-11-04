import os
import pathlib
import shutil

fileFormat = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".rar"]
}

for file in os.scandir():
    
    if file.is_dir():
        print(f"{file.name} is a directory, skipping.")
        continue

    fileName = pathlib.Path(file)
    fileFormatType = fileName.suffix.lower()
    print(f"Processing {fileName}")

    
    dest_folder = "Other"
    if fileFormatType == "":
        print(f"{fileName} has no file format, moving to {dest_folder}")
    else:
        
        for folder, formats in fileFormat.items():
            if fileFormatType in formats:
                dest_folder = folder
                print(f"{fileName} matched category {dest_folder}")
                break

    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    
    shutil.move(str(fileName), os.path.join(dest_folder, fileName.name))
    print(f"Moved {fileName} to {dest_folder}")
