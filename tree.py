import os

def tree(dir_path, prefix=""):
    items = os.listdir(dir_path)
    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            tree(path, prefix + extension)

tree(".")
