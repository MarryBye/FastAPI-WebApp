import os

# def recursive_get_files(path):
#     files = []
#     for element in os.listdir(path):
#         path_to_element = os.path.join(path, element)
#         if os.path.isdir(path_to_element):
#             files.extend(recursive_get_files(path_to_element))
#         else:
#             files.append(element)
#     return files

class QueriesController:
    def __init__(self):
        self.queries = self.get_sql_scripts(os.path.join("./core/sql/"))
        
    def get_sql_scripts(path):
        scripts = {}
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                file = open(os.path.join(root, filename), "r", encoding="UTF-8")
                scripts[filename] = file.read()
                file.close()
        return scripts
    
    def get_query(self, name):
        return self.queries.get(name, None)