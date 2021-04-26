import sys
import os
import glob


class ScriptGenerator:
    def __init__(self, project, dependencies):
        self.project = project
        self.dependencies = dependencies

    def generate_scripts(self):
        self.clean_project_folder()

        for dependency in self.dependencies:
            self.generate_single_script(dependency)

    def clean_project_folder(self):
        files = glob.glob("Project Data/" + self.project + '/Builder/Dependencies/*')
        for f in files:
            os.remove(f)

    def generate_single_script(self, dependency):
        file = open("Project Data/" + self.project + '/Builder/Dependencies/' + dependency.name + ".py", 'w')
        sys.stdout = file

        print("import pyautogui")
        print("")

        for observation in dependency.observation_list:
            self.translate_observation_to_script_command(observation)

        file.close()

    @staticmethod
    def translate_observation_to_script_command(observation):
        if observation.data_type == "imgPoint":
            print("pyautogui.click(x=100, y=200)")
        elif observation.data_type == "Keypresses":
            string_to_print = ""
            for char in observation.data["content"]:
                if char == "[":
                    print("pyautogui.write(\"" + string_to_print + "\")")
                    string_to_print = "["
                elif char == "]":
                    string_to_print = string_to_print + "]"
                    print("pyautogui.write(\"" + string_to_print + "\")")
                    string_to_print = ""
                else:
                    string_to_print = string_to_print + char
            if len(string_to_print) > 0:
                print("pyautogui.write(\"" + string_to_print + "\")")






