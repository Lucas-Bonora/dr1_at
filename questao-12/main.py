import os

def list_files_recursive(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            print(full_path)

root_directory = '/caminho/ficticio/para/pasta'
list_files_recursive(root_directory)
