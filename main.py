# main.py
# the entry point for the program.
from naming import names_to_dir
from sorting import extract

def parser():
    pass


def main():
    main_directory = extract.getDirectory()
    
    names_to_dir.byCountry(main_directory)  

    # check if user wants to create subdirectories
    custom_terms = names_to_dir.sortByUserValues()
    
    names_to_dir.sortZips({}, main_directory, custom_terms, sortingSubDirectories=True)    
    
    extract.extractZipFiles(main_directory)
    extract.deleteZipFiles(main_directory)

if __name__ == "__main__":
    main()