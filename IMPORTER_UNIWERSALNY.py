import subprocess
import os
import json
import shutil

class UniversalImporter:
    # ... (pozostałe metody klasy pozostają bez zmian)

    def copy_file_to_importers(self, filename):
        source_path = os.path.join(current_directory, filename)
        destination_path = os.path.join(self.script_directory, filename)
        if os.path.exists(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"{filename} wczytane.")
        else:
            print(f"Plik {filename} nie istnieje w bieżącym katalogu.")

    def choose_and_run(self):
        # Wyświetl komunikat powitalny
        print("IMPORTER UNIWERSALNY. UTWÓRZ PLIK wykazy.xlsx")

        # Pytanie o wczytanie pliku wykazy.xlsx
        choice = input("Czy wczytać plik wykazy.xlsx? [y/n]: ").lower()
        if choice == 'y':
            self.copy_file_to_importers('wykazy.xlsx')
        elif choice == 'n':
            print("Zakończenie działania programu.")
            return
        else:
            print("Nieprawidłowy wybór.")
            return

        # Wyświetl listę dostępnych importerów
        self.list_scripts()
        try:
            script_choice = int(input("Wpisz numer skryptu, który chcesz uruchomić lub 'KOPIUJ XML': "))
            self.run_script(script_choice)
        except ValueError:
            print("Proszę wpisać numer.")
        except IndexError:
            print("Nieprawidłowy numer skryptu.")

# Użycie:
current_directory = os.path.dirname(os.path.abspath(__file__))
scripts_directory = os.path.join(current_directory, 'IMPORTERY')
json_filename = 'scripts.json'

importer = UniversalImporter(scripts_directory, json_filename)
importer.choose_and_run()
