from component_manager import ComponentManager
import argparser
import actions
import os
# import remove
# import push

GODOT_COMPONENTS_DIR = "/home/tohru/Drive/godot/godot-resources/components"


def main():

    current_dir = '/home/tohru/tmp/frog_survivor'
    project_manager = ComponentManager(
        current_dir, os.path.join(current_dir, "components"))
    components_manager = ComponentManager(
        GODOT_COMPONENTS_DIR, GODOT_COMPONENTS_DIR)

    args = argparser.parse_args()

    action = args.action
    files = "file1"
    if action == 'add':
        actions.handle_add(files, components_manager, project_manager)

    elif action == 'push':
        actions.handle_push("Hahaha", components_manager, project_manager)

    elif action == 'list':
        actions.handle_list(project_manager)


if __name__ == "__main__":
    main()
