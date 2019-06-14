import sys
import os
import getopt
from subprocess import call
import languages
import config

version = 0.1

help_text = 'proman [[-l <language name>] new <project name>] [-h, --help] [-v, --version]'

def create_project(name, language):
    # Get styled name for language
    name = language.getStyledName(name)

    # Check if base project directory exists:
    if not os.path.isdir(config.project_dir):
        os.mkdir(config.project_dir)
    
    # Check if language directory exists
    lpath = os.path.join(config.project_dir, language.folder_name)
    if not os.path.isdir(lpath):
        os.mkdir(lpath)

    # Check if project already exists
    ppath = os.path.join(lpath, name)
    if os.path.isdir(ppath):
        print("Error: Project already exists.")
        exit()
    
    # Make project directory
    os.mkdir(ppath)
    language.create(name, ppath)

    # Change into project directory and call 'open_command' in project folder
    os.chdir(ppath)
    call(config.open_command.split(' '))

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hlv:", ["language=","version"])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    
    language = None

    # Get options
    for opt,arg in opts:
        if opt in ('-h', '--help'):
            print(help_text)
        elif opt in ('-v', '--version'):
            print("Proman Version {}".format(version))
        elif opt in ('-l', '--language'):
            language = languages.get(arg)
            print("Entered language")
            if(language == None):
                print("Error: Language doesn't exist.")
                print("Please select one from the following list:")
                language = languages.get_language_from_user()
            
    if(len(argv) >= 2):
        if(argv[-2] == 'new'):
            # Create new project
            name = argv[-1]

            if language == None:
                language = languages.get_language_from_user()

            create_project(name, language)
        else:
            print("Error: Unknown command.")
            print(help_text)
    elif(len(argv) == 1):
        if(argv[-1] == 'new'):
            print("Error: Project name must be given.")

if __name__ == "__main__":
    main(sys.argv[1:])
    