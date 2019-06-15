import toml
import os
import util

CONFIG_FILE = "config.toml"

# Performs first time setup and creates a config file with all required fields


def firstTimeSetup():
    print("Proman - First time setup:")
    print("--------------------------")
    print("Leave blank to use default value; (default).")
    print()

    c = {}

    # Get path to root project folder
    d = os.path.expanduser("~/Projects")
    c['projects_path'] = util.inputWithDefault(
        "Projects Path({}): ".format(d), d)

    # Get command to run when a project is created/opened
    d = "code ."
    c['open_command'] = util.inputWithDefault(
        "Open Command ({}): ".format(d), d)

    # Write config to file
    f = open(CONFIG_FILE, "w")
    f.write(toml.dumps(c))
    f.close()

    print()
    print("Configuration complete.")


# Check if first time setup needs to be run
if not os.path.isfile(CONFIG_FILE):
    # No config file exists, run first-time-setup
    firstTimeSetup()

# Read config file
f = open(CONFIG_FILE, "r")
config = '\n'.join(f.readlines())
config = toml.loads(config)
f.close()

# Returns the given config setting


def get(setting):
    return config[setting]

# Returns the given config setting for language


def getlang(language, setting):
    v = get(setting)

    if language.title in config:
        if setting in config[language.title]:
            v = config[language.title][setting]

    return v
