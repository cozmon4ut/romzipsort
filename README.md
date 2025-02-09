# romzipsort
This is a utility for sorting large amounts of zip files, commonly found in ROM sets.

# How It Works
The user is asked for the directory to sort, and then the program will do an initial scan to obtain all of the names of the zip files; **The zip files must be in the directory given.** It will look for country terms in the zip file's name, following a hard-coded format of typically found abbreviations. It will then create folders and sort them by country.

The user is asked if they'd like to create their own folders with their own keywords to search. It will create the subdirectories and move the files there. 

Finally, it extracts them, and deletes the zip files.

# Notes
This program is a WIP, command-line arguments will be added to manipulate the normal control flow (read terms from users' JSON instead of hard-coded values, skip certain steps, etc.)
