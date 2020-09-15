# organizing all file in folder random-file
import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

# function that return category based on the file suffixes
def pickDirectory(value):
    # loop the item in the dictionaries
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            #if suffix found, return the category
            if suffix == value:
                return category
    return 'MISC'
print(pickDirectory('.pdf'))

# function for organizing directory
def organizeDirectory():
    # loops all the files
    for item in os.scandir():
        if item.is_dir():
            continue
        # retrieve the path of each item
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

