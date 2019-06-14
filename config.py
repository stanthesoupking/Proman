import toml
import os
import util

CONFIG_FILE = "config.toml"


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

    d = "code ."
    c['open_command'] = util.inputWithDefault(
        "Open Command ({}): ".format(d), d)

    f = open(CONFIG_FILE, "w")
    f.write(toml.dumps(c))
    f.close()

    print()
    print("Configuration complete.")


if not os.path.isfile(CONFIG_FILE):
    # No config file exists, run first-time-setup
    firstTimeSetup()

# Read config file
f = open(CONFIG_FILE, "r")
config = '\n'.join(f.readlines())
config = toml.loads(config)
f.close()

def get(setting):
    return config[setting]