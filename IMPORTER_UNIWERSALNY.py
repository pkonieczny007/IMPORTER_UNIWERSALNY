import subprocess
import os
import json
import shutil

class UniversalImporter:
    def __init__(self, script_directory, json_filename):
        self.script_directory = script_directory
        self.json_filename = json_filename
        self.scripts = self.load_scripts()

    def load_scripts(self):
        # Wczytaj skrypty z pliku JSON z określeniem kodowania UTF-8
        json_path = os.path.join(self.script_directory, self.json_filename)
        with open(json_path, 'r', encoding='utf-8') as file:
            scripts_data = json.load(file)
        return scripts_data

    def list_scripts(self):
        # Wyświetl listę skryptów z numerami do wyboru
        print("Dostępne skrypty:")
        for index, script in enumerate(self.scripts, start=1):
            print(f"{index}. {script}")
        print(f"{len(self.scripts) + 1}. KOPIUJ XML")

    def run_script(self, script_number):
        # Uruchom wybrany skrypt Pythona
        if script_number == len(self.scripts) + 1:
            self.copy_xml_files()
        else:
            script_name = list(self.scripts.keys())[script_number - 1]
            instructions = self.scripts[script_name]
            print(f"Instrukcje dla skryptu: {instructions}")
            input("Naciśnij Enter, aby kontynuować...")
            script_path = os.path.join(self.script_directory, script_name)
            print(f"Uruchamianie skryptu: {script_name}")
            subprocess.run(['python', script_path], shell=True)
            print(f"Zakończono uruchamianie skryptu: {script_name}")

    def copy_xml_files(self):
        # Kopiuj wszystkie pliki XML z katalogu IMPORTERY do katalogu skryptu UniversalImporter
        xml_files = [f for f in os.listdir(self.scripts_directory) if f.endswith('.xml')]
        for xml_file in xml_files:
            source_path = os.path.join(self.scripts_directory, xml_file)
            destination_path = os.path.join(current_directory, xml_file)
            shutil.copy2(source_path, destination_path)
        print("Wszystkie pliki XML zostały skopiowane.")

    def choose_and_run(self):
        # Pozwól użytkownikowi wybrać skrypt do uruchomienia
        self.list_scripts()
        try:
            choice = int(input("Wpisz numer skryptu, który chcesz uruchomić lub 'KOPIUJ XML': "))
            self.run_script(choice)
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
