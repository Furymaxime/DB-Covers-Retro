import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if name.lower().endswith(", the"):
            new_name = "The " + name[:-5] + ext
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")
        else:
            print(f"File '{filename}' does not match the pattern")

if __name__ == "__main__":
    directory = input("Entrez le chemin du dossier : ")
    if os.path.isdir(directory):
        rename_files_in_directory(directory)
    else:
        print("Le chemin spécifié n'est pas un dossier valide.")