#importing libraries
from pathlib import Path
import re


def checks_path(path):
    #checks to seee that you gave a valid windwos path. NOT that it exists that the chars used are valid.
    invalid = r'[<>";?|.*]'
    if re.search(invalid, path):
        return False
    if re.match(r'^[A-Z]:\\', path, re.IGNORECASE):
        return True
    return False


while True:
    mypath = input("Pleae tell me the path you wish add a subfoldler too: ")
    if checks_path(mypath):
        break
    print("Please only input a valid Windows path.")
