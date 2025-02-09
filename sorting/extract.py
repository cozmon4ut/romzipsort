# extract.py
# For extraction
from zipfile import ZipFile
from pathlib import Path
from os import remove

# Obtains the appropriate directory from the user
def getDirectory() -> Path: 
    # Loop while getting input 
    while True:
        directory = Path(input("Please enter the directory to sort: ")) 
        if not directory.exists():
            print(f"\nThe inputted directory was not found.")
            continue
        else:
            break
    
    return directory
        
    


# Extracts zip files from the given directory        
def extractZipFiles(directory: Path): 
    # Ensure directory is valid
    if not directory.is_dir():
        print(f"{directory} is invalid")
        return
    
    # Iterate through each folder in the directory
    for subfolder in directory.rglob("*"):
        # Check if it's a directory
        if subfolder.is_dir():
            print(f"Checking folder: {subfolder}")
            
            # Iterate through each zip in the subfolder
            for zip_file in subfolder.glob("*.zip"):
                try:
                    # Open the zip file and extract its contents into the same subfolder
                    with ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(subfolder)
                        print(f"Extracted {zip_file.name} into {subfolder}")
                
                except Exception as e:
                    print(f"Failed to extract {zip_file.name} in {subfolder}: {e}")
            
                
# For clean-up purposes
def deleteZipFiles(directory: Path):
    for subfolder in directory.iterdir():
        for zip_file in subfolder.rglob("*.zip"):
            try:
                remove(zip_file)
            except Exception as e:
                print(f"Failure cleaning up: {e}")
                