import argparse
from component_manager import ComponentManager
import add
# import remove
# import push

GODOT_COMPONENTS_DIR = "/home/tohru/Drive/godot/components"


def main():
    parser = argparse.ArgumentParser(prog='gdcomp',
                                     description='Handle godot components',
                                     epilog='Text at the bottom of help')

    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    # define 'list' action
    list_parser = subparsers.add_parser('remove',
                                        help='list avaliable components')
    # remove_parser.add_argument('files', nargs='+', help='File(s) to remove')
    # define 'add' action
    add_parser = subparsers.add_parser('add',
                                       help='add a component to the project')
    add_parser.add_argument('files', nargs='+', help='File(s) to add')
    # define 'remove' action
    remove_parser = subparsers.add_parser(
        'remove', help='remove a component from the current project')
    remove_parser.add_argument('files', nargs='+', help='File(s) to remove')
    # define 'push' action
    push_parser = subparsers.add_parser(
        'push', help='update a component and push to git repo')
    push_parser.add_argument(
        'files',
        nargs='+',
        help='update the component to match the one on the current project')

    parser.set_defaults(action="list")

    args = parser.parse_args()

    manager = ComponentManager(GODOT_COMPONENTS_DIR)

    action = args.action
    try:
        files = args.files
    except:
        print("bruh")


    if action == 'add':
        add.handle(files, manager)

    elif action == 'remove':
        print(f'Removing files: {files}')

    elif action == 'push':
        print(f'Pushing files: {files}')

    elif action == 'list':
        print("listing")


if __name__ == "__main__":
    main()