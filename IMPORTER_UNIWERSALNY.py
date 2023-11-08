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
        json_path = os.path.join(self.script_directory, self.json_filename)
        with open(json_path, 'r', encoding='utf-8') as file:
            scripts_data = json.load(file)
        return scripts_data

    def list_scripts(self):
        print("Dostępne skrypty:")
        for index, script in enumerate(self.scripts, start=1):
            print(f"{index}. {script}")
        print(f"{len(self.scripts) + 1}. KOPIUJ XML")
        print(f"{len(self.scripts) + 2}. WGRAJ wykaz.xlsx")

    def run_script(self, script_number):
        if script_number == len(self.scripts) + 1:
            self.copy_xml_files()
        elif script_number == len(self.scripts) + 2:
            self.upload_wykaz_file()
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
        xml_files = [f for f in os.listdir(self.script_directory) if f.endswith('.xml')]
        for xml_file in xml_files:
            source_path = os.path.join(self.script_directory, xml_file)
            destination_path = os.path.join(current_directory, xml_file)
            shutil.copy2(source_path, destination_path)
        print("Wszystkie pliki XML zostały skopiowane.")

    def upload_wykaz_file(self):
        print("Wgrano wykaz.xlsx do systemu.")

    def copy_file_to_importers(self, filename):
        source_path = os.path.join(current_directory, filename)
        destination_path = os.path.join(self.script_directory, filename)
        if os.path.exists(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"{filename} wczytane.")
        else:
            print(f"Plik {filename} nie istnieje w bieżącym katalogu.")

    def choose_and_run(self):
        print("IMPORTER UNIWERSALNY. UTWÓRZ PLIK wykaz.xlsx")
        choice = input("Czy wczytać plik wykaz.xlsx? [y/n]: ").lower()
        if choice == 'y':
            self.copy_file_to_importers('wykaz.xlsx')
        elif choice == 'n':
            print("Zakończenie działania programu.")
            return
        else:
            print("Nieprawidłowy wybór.")
            return

        while True:
            self.list_scripts()
            print("Wpisz c aby zamknąć.")
            user_input = input("Wybierz opcję: ").lower()
            if user_input == 'c':
                print("Zamykanie programu.")
                break
            try:
                script_choice = int(user_input)
                self.run_script(script_choice)
            except ValueError:
                print("Proszę wpisać numer lub 'c' aby zamknąć.")
            except IndexError:
                print("Nieprawidłowy numer skryptu.")

# Użycie:
current_directory = os.path.dirname(os.path.abspath(__file__))
scripts_directory = os.path.join(current_directory, 'IMPORTERY')
json_filename = 'scripts.json'

importer = UniversalImporter(scripts_directory, json_filename)
importer.choose_and_run()
