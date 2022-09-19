import os

# GLOBALS
SCRIPT_ROOT_DIR = os.path.dirname(os.path.abspath("__file__"))
DATABASE = os.path.join(SCRIPT_ROOT_DIR, "database")
filename = "lmao"


def check_dir(name):
    print('checking database and file\n')  # Press Ctrl+F8 to toggle the breakpoint.
    if not os.path.exists(DATABASE):
        print("Database directory not found.\n")
        return 404


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting script\n')
    os.chdir(SCRIPT_ROOT_DIR)

    open(filename)


