import sys
import os
import glob


class ScriptGenerator:
    def __init__(self, project, dependencies):
        self.project = project
        self.dependencies = dependencies
        self.observation_list = []
        self.generate_observation_list()


    def generate_observation_list(self):
        index = 1
        for dependency in self.dependencies:
            for observation in dependency.observation_list:

                observation.observation_number = index
                index = index + 1
                if observation.user_action:
                    self.observation_list.append(observation)


    def generate_scripts(self):
        self.clean_project_folder()

        temp = sys.stdout

        for observation in self.observation_list:
            self.generate_single_script(observation)

        sys.stdout = temp 

    def clean_project_folder(self):
        files = glob.glob("Project Data/" + self.project + '/Runner/Scripts/*')
        for f in files:
            os.remove(f)

    def generate_single_script(self, observation):
        file = open("Project Data/" + self.project + '/Runner/Scripts/observation' + str(observation.observation_number) + ".py", 'w')
        sys.stdout = file

        print("import pyautogui")
        print("")

    
        self.translate_observation_to_script_command(observation)

        file.close()

    def translate_observation_to_script_command(self, observation):
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
                    print("pyautogui.press(\"" + self.translate_key(string_to_print) + "\")")
                    string_to_print = ""
                elif char == "\"":
                    print("pyautogui.write(\"" + string_to_print + "\")")
                    string_to_print = ""
                else:
                    string_to_print = string_to_print + char
            if len(string_to_print) > 0:
                print("pyautogui.write(\"" + string_to_print + "\")")

    def translate_key(self, string):
        if string == "[Return]":
            return "enter"
        elif string == "[Control_L]" or string == "[Control_R]":
            return "ctrl"
        elif string == "[Shift_L]" or string == "[Shift_R]":
            return "shift"
        # elif string == "[Control_L]" or string == "[Control_R]":
        #     return "ctrl"
        # elif string == "[Control_L]" or string == "[Control_R]":
        #     return "ctrl"
        # elif string == "[Control_L]" or string == "[Control_R]":
        #     return "ctrl"
        # elif string == "[Control_L]" or string == "[Control_R]":
        #     return "ctrl"
        else:
            return string[1:-1]
        






