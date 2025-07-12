# Napisz program, który:
# Przechodzi po wszystkich plikach .py w bieżącym folderze.
# Jeśli nazwa pliku zawiera -, zmienia go na _.
# Zamienia nazwę pliku fizycznie na dysku (os.rename(...)).

# 🧠 Wskazówki:
# użyj os.listdir() do pobrania nazw plików,
# filtruj tylko te, które kończą się .py,
# sprawdź, czy w nazwie jest "-",
# zbuduj nową nazwę przez .replace("-", "_"),
# użyj os.rename(stara, nowa) do przemianowania.

import os

def change_files_names():
    for folder_path, _, files in os.walk("."):
        for filename in files:
            if "-" in filename:
                new_name = filename.replace("-", "_")
                os.rename(filename, new_name)
                print(filename)

change_files_names()