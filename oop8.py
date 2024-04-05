import os

class Cd:
    def __init__(self, new_dir):
        if not os.path.isdir(new_dir):
            raise ValueError("The specified directory does not exist or is not a directory.")
        self.new_dir = os.path.abspath(new_dir)
        self.old_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.old_dir)

try:
    with Cd("/home"):
        print("Current directory after entering the context: ", os.getcwd())
    print("Current directory after exiting the context:", os.getcwd())
except ValueError as e:
    print(e)