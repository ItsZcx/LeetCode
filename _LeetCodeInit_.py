#!/usr/bin/env python3

############################################################
# Script to build a problem directory with this structure: #
#                                                          #
#                    . [problem_name]                      #
#                    ├── README.md                         #
#                    ├── [problem_name].py                 #
#                    └── others                            #
#                         ├── .gitignore                   #
#                         └── ...                          #
#                                                          #
############################################################

import os
from typing import *
from colorama import Fore, Style

# Print error msg
def inputError():
    print('Write "' +
        Fore.GREEN + '1' +
        Style.RESET_ALL+'", "' +
        Fore.LIGHTYELLOW_EX + '2' +
        Style.RESET_ALL+'" or "' +
        Fore.RED + '3' +
        Style.RESET_ALL+'", please.')

# Aks for problem difficulty and return it as a string
def getDifficulty():
    try:
        difficulty: int = int(input("Which difficulty is the problem rated as?\n" +
            Fore.GREEN + " - Easy -> 1\n" +
            Fore.LIGHTYELLOW_EX + " - Medium -> 2\n" +
            Fore.RED + " - Hard -> 3\n"+
            Style.RESET_ALL + "--> "))
        if (difficulty < 1 or difficulty > 3):
            raise ValueError

    except ValueError:
        inputError()
        exit(-1)

    if difficulty == 1:
        return "Easy"
    elif difficulty == 2:
        return "Medium"
    else:
        return "Hard"

# Remove first space in a string
def removeFirstSpace(name: str):
    spacePos: int = name.find(' ')

    if spacePos != -1 and name[spacePos - 1] == ".":
        return name[:spacePos] + name[spacePos + 1:]
    else:
        return name

# Get problem number and name
def getName():
    name: str = input('\nPlease write the number as well as the name of the problem.\n - Ex: "1. Two Sum"\n--> ')
    name = removeFirstSpace(name)
    return name

# Creates directories
def createDirStructure(finalPath: str):
    # Create folder if the problem doesn't exist
    if os.path.isdir(finalPath) == False:
        os.mkdir(finalPath)
        finalPath = finalPath + "/others"
        os.mkdir(finalPath)
        return True
    return False

# Creates and fills files
def createFiles(finalPath: str, name: str):
    readmePath:       str = finalPath + "/README.md"
    readmeContent:    str = "Change for Clip LeetCode Markdown"
    pyPath:           str = finalPath + "/" + name[name.find(".") + 1:] + ".py"
    pyContent:        str = "#!/usr/bin/env python3\nfrom typing import *\n\n#* All tests passed --- x/x passed\n"
    gitignorePath:    str = finalPath + "/others/.gitignore"
    gitignoreContent: str = "../.vscode/\n"

    # Create readme
    with open(readmePath, 'w') as _readme:
        _readme.write(readmeContent)

    # Create .py + give permissions
    with open(pyPath, 'w') as _pyPath:
        _pyPath.write(pyContent)
        os.chmod(pyPath, 0o755)

    # Create .gitignore
    with open(gitignorePath, 'w') as _gitignorePath:
        _gitignorePath.write(gitignoreContent)

# Build structure
def createStructure(difficulty: str, name: str):
    currDir = os.getcwd()
    name = name.replace(" ", "_")
    finalPath: str = "/".join([currDir, difficulty, name])

    successDirs = createDirStructure(finalPath)
    if successDirs == True:
        createFiles(finalPath, name)

def main():
    difficulty: str = getDifficulty()
    name: str = getName()
    createStructure(difficulty, name)
    print("\nInitialization finished!")

if __name__ == "__main__":
    main()