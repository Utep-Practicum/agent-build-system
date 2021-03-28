import os
import json

class BuilderBackEnd:

    def read_relationships(self):
        """
        Read each Relationship file
        """
        directory = "../Causation_Extractor/relationships"
        files_list = os.listdir(directory)
        relationships_list = []
        #formated_relations = []
        dictionary_relations = {}

        # Read each relationship file and add it to a list
        for file in files_list:
            with open(directory + "/" + file, 'r') as relacion:
                relationships_list.append(json.load(relacion))

        # For each list in the list enumerate it to create the name of each Relationship and add it to a new list
        for index, relation in enumerate(relationships_list, start=1):
            dictionary_relations["Relation " + str(index)] = relation
            #formated_relations.append(["Relation " + str(index), relation])

        return dictionary_relations

#
# if __name__ == "__main__":
#     bb = BuilderBackEnd()
#     bb.read_relationships()