from pathlib import Path
import os 

def rename_the_files(target_folder, remove_str):
    for items in target_folder.iterdir():
        if not items.is_dir():
            kenshi_stripper(items, remove_str)
        else:
            for file in items.iterdir():
                if file.is_file:
                    kenshi_stripper(file, remove_str)

        
def kenshi_stripper(file_path, remove_str):
    stem = file_path.stem
    suffix = file_path.suffix
    cleaned_stem =(
        stem
        .replace(f"_{remove_str}_","_")
        .replace(f"_{remove_str}","")
        .replace(f"_{remove_str}","")
        .replace(f" {remove_str} ","")
        .replace(f"{remove_str} ","")
        .replace(f" {remove_str}","")
        .replace(remove_str,"")
        .strip()
    )
    cleaned_name = f"{cleaned_stem}{suffix}"

    if cleaned_name != file_path.name:
        new_file_path = file_path.with_name(cleaned_name)
        file_path.rename(new_file_path)
        print(f"Renamed: {file_path.name} to {cleaned_name}")

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
print("-"*50)

test_folder = Readme_path.parent / "test_names"
bad_str =input("What string do you want to remove from the files? = ")

rename_the_files(test_folder,bad_str)