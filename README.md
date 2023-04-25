

# gdcomp: Godot Components Manager

This is a command-line utility made in python for managing components for the Godot Engine. A component is a script (and optionally a scene) that can be added to a Godot project. This utility allows you to add components to a project, push updates to the global components repository, list components, and manage the configuration file. It's a wrapper to avoid using long `cp` or `git` commands all the time when working with components.

It supports:

- git integration
- fuzzy search

## Installation
### Dependencies 
Go the the project dir and make sure venv environment is activated.
```
pip install pyinstaller colorama configparser fuzzywuzzy Levenshtein
```

### Build
Create the executable.

```
./venv/bin/pyinstaller --name gdcomp main.py --onefile
```

Change permissions and copy to `/home/.local/bin`.

```
chmod +x ./dist/gdcomp && cp ./dist/gdcomp ~/.local/bin
```


## Usage

To use gdcomp, navigate to the root directory of your Godot project and run one of the following commands:

- `gdcomp add <compname>`: Adds the specified component to your project's components directory. The component must exist in the global components repository, which is located at `/home/godot_components` as default, but can be changed by editing the file. If <compname> has some typo, it will suggest the best match.

- `gdcomp push <compname>`: Pushes any changes made to components in your project to the global components repository.

- `gdcomp ls [-p]`: Lists the components in the global components repository. If the `-p` option is passed, lists components in the current project's components directory instead. It's the default

- `gdcomp config`: Displays information about the configuration file and the current locations for the project and components.

## Configuration

The configuration file is located at `/home/.config/gdcomp/conf.ini`. You can edit this file to change the location of your components directory.

```
[global]
components_dir = /home/{username}/godot_components
```