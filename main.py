from component_manager import ComponentManager
import argparser
import actions
import os

# import remove
# import push

GODOT_COMPONENTS_DIR = "/home/tohru/Drive/godot/godot-resources/components"


def main():
    current_dir = "/home/tohru/tmp/newgodot"
    current_dir = os.getcwd()
    #
    project_manager = ComponentManager(
        current_dir, os.path.join(current_dir, "components")
    )
    components_manager = ComponentManager(GODOT_COMPONENTS_DIR, GODOT_COMPONENTS_DIR)

    args = argparser.parse_args()

    action = args.action
    if action == "add":
        actions.handle_add(args.base_name, components_manager, project_manager)

    elif action == "push":
        actions.handle_push(args.base_name, components_manager, project_manager)

    elif action == "ls":
        if args.project_dir:
            actions.handle_list(project_manager)
        else:
            actions.handle_list(components_manager)

    elif action == "config":
        actions.handle_config(components_manager, project_manager)


if __name__ == "__main__":
    main()
