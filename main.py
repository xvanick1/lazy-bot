import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform


# GLOBALS
SCRIPT_ROOT_DIR = os.path.dirname(os.path.abspath("__file__"))


def check_file_exist(file_path):
    if not os.path.exists(file_path):
        print("File not found.\n")
        return 404


def input_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file",  help="Loads filename properties", type=str)
    arg = parser.parse_args()
    return arg.file


def check_platform():
    if platform.system() == "Linux":
        return os.path.join(SCRIPT_ROOT_DIR, "chromedriver", "chromedriver_linux")
    elif platform.system() == "Windows":
        return os.path.join(SCRIPT_ROOT_DIR, "chromedriver", "chromedriver.exe")
    elif platform.system() == "Darwin":
        return os.path.join(SCRIPT_ROOT_DIR, "chromedriver", "chromedriver")
    else:
        print("Unable to identify your OS")
        exit(404)


if __name__ == '__main__':
    print('Starting script\n')
    os.chdir(SCRIPT_ROOT_DIR)  # change directory to the project root
    filename = input_parser()
    filepath = os.path.join(SCRIPT_ROOT_DIR, filename)  # get file path
    check_file_exist(filepath)  # check that file exists
    platform = check_platform()  # check platform

    driver = webdriver.Chrome(executable_path=platform)
    driver.get("http://is.muni.cz")

    input("Log into IS and open specific Ropot. Then press Enter to continue...")

    # Open file from file_path and read it line by line
    with open(filepath, 'r') as f:
        for line in f:
            inputElement = driver.find_element(By.XPATH, "//input[starts-with(@id, 'tst_')]")
            inputElement.send_keys(line)

    f.close()
    print("End of file. Check the answers and submit.")








