from Relation import *

class Controller:
    def __init__(self):
        self.relationships_main = []
        self.dependencies_main = []


    def add_relationship(self, relationship):
        """
        # Import relationships into the controller
        """
        self.relationships_main.append(Relation(relationship))

    
    def move_to_dependency(self, relationship_name):
        """
        # Removes relationship from relationship list and translates to dependency list
        """
        self.dependencies_main.append(self.relationships_main.pop(self.relationships_main.index(relationship_name)))

    
    def move_to_relationship(self, relationship_name):
        """
        # Removes dependency from dependency list and translates to relationship list
        """
        self.relationships_main.append(self.dependencies_main.pop(self.dependencies_main.index(relationship_name)))


    def get(self, keyword = '', table = 'relationships'):
        search = []
        if table.lower() == 'relationships':
            if keyword == '' or keyword == None:
                return self.relationships_main
            else:
                for relation in self.relationships_main:
                    for item in relation:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search
        elif table.lower() == 'dependencies':
            if keyword == '' or keyword == None:
                return self.dependencies_main
            else:
                for relation in self.dependencies_main:
                    for item in relation:
                        if keyword in item.show():
                            search.append(relation)
                            break
                return search