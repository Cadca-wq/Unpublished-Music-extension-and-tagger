from pathlib import Path
import os 

def list_all_the_dir(directory):
    ls = [x for x in directory.iterdir()]
    print(ls)
# this finds the path where name_changer.py sits, gets its parent dir and uses that to initialise the readme into a variable 
Readme_path = Path(__file__).parent/ "README.md"

anime_dir = Readme_path.parent.parent / "Durarara"
# durarara is the folder i want to access
print(anime_dir)
if anime_dir.is_dir():
    list_all_the_dir(anime_dir)

list_all_the_dir(Readme_path.parent / "test_names")