# Proman
Project manager that organises projects by their programming language and name.

## Dependencies
This code was designed to run with the latest version of Python (3.7.2 at time
of writing).
### Libraries
Before running Proman, you will need to install its dependencies by running the
following code:  
`pip install toml`

## Setup
If you want easy access to Proman from any directory in your terminal, you may
want to set the following alias in your `.bash_profile` file:  
`alias proman='python3 <path to Proman/main.py>'`

### Custom Configuration
The configuration file, 'config.toml' can be edited to create custom profiles
for each language.  
  
*For example:*  
Setting *C* projects to open using the command, `"vim ."`:  
**config.toml**
```
[C]
open_command = "vim ."
```

## Usage
`proman [[-l <language name>] new <project name>] [-h, --help] [-v, --version]`

*For example:*  
Creating a new project called "Example Project" in the C langauge, would be as
follows:  
`proman --language c new "Example Project"`