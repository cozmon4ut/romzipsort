# names_to_dir.py
# Looks at all zips and sorts them into the appropriate directory.
import shutil
from pathlib import Path

# Function for getting the name of each and every zip file.
def getZipNames(directory: Path) -> list:
    if not directory.is_dir():
        print(f"{directory} is invalid.")
        return []
    
    # Collect the names of every zip file in the base directory
    zip_files = list(directory.glob("*.zip"))
        
    print(f"Found {len(zip_files)} zip files")    
    
   
    return zip_files

# Function for moving the zips and creating directories
def move(zip_names, base_directory: Path, terms:dict): 
    # Given each zip name, iterate over them
    for zip in zip_names: 
        # Make a variable for the name of the zip, and one for matching the dictionary term with it
        zip_name = zip.name  
        match = None 
        
        # If there are terms present, look for a match 
        if terms:
            for key, values in terms.items():
                for value in values:
                    if value in zip_name:
                        match = key
                        break
                if match: # Break match here so it can be accessed later
                    break
            
            # With match variable, begin creating directories 
            if match:
                new_dir = base_directory / match
                new_dir.mkdir(parents=True, exist_ok=True)
                
                # Move files
                dest = new_dir / zip.name
                shutil.move(zip, dest)
                
                print(f"Moved {zip} to {dest}") 
        

# Function for sorting zips 
def sortZips(zip_names, base_directory: Path, terms: dict, sortingSubDirectories: bool): 
    if sortingSubDirectories:
        for subfolder in [d for d in base_directory.iterdir() if d.is_dir()]:
            zip_names = getZipNames(subfolder)
            
            move(zip_names, subfolder, terms)
    else:
        move(zip_names, base_directory, terms) 
   


# Function for sorting by country
def byCountry(base_directory: Path):
    
    # Follows the format {k: []}, where the list contains countries listed in rom sets
    # May not cover edge cases, only based on what I saw consistently in the filenames 
    countries_dict = {
        "USA": 
            ["(USA)", "(USA, Europe)", "(USA, Japan)","(Japan, USA)", "(En, Ja)"],
        "EN/NTSC/MPAL/PAL": 
            ["(En)","(NTSC)","(MPAL)","(PAL)"],
        "Europe": 
            ["(Europe)", "(Europe, Australia)"],
        "Japan":
            ["(Japan)"],
        "France":
            ["(France)"],
        "Germany":
            ["(Germany)"],
        "Italy":
            ["(Italy)"],
        "Spain":
            ["(Spain)"],
        "Brazil":
            ["(Brazil)"],
        "Australia": 
            ["(Australia)"],
        "Asia": 
            ["(Asia)"],
        "World/Universal/Unknown": 
            ["(World)","(Unl)", "(Unknown)"],
    }
        
    zip_names = getZipNames(base_directory)
      
    sortZips(zip_names, base_directory, countries_dict, sortingSubDirectories=False)
    


# Function that lets the user specify what folders should be named
def sortByUserValues():
   
    # make dict
    user_terms = {}
    
    # start loop for input
    while True:
        key = str(input("(q to quit) Enter the name of the folder you want created: "))
        
        if key != "q":
            value = str(input('Enter the word to search for (example: "Zelda" to specifically look for file names containing Zelda): '))
            user_terms[key] = [value]
            print(user_terms)
        
        else:
            break
    
    return user_terms 
        
         
        
         




# TODO Function for sorting by release type.
def byReleaseType(base_directory: Path):
    # Possible release types. May not be conclusive
    release_type = ["LodgeNet", "Demo", "Kiosk", "Proto", "Aftermarket"
                    "Uni", "Beta", "Test Program", "Rev", "BIOS"]

# TODO Function for sorting by Everdrive compatibility 
def byCompatibility():
    pass



