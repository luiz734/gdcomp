import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='gdcomp',
                                     description='Handle godot components',
                                     epilog='Text at the bottom of help')

    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    list_parser = subparsers.add_parser(
        'list', help='list avaliable components')

    add_parser = subparsers.add_parser(
        'add', help='add a component to the project')
    add_parser.add_argument('files', nargs='+', help='Components(s) to add')

    push_parser = subparsers.add_parser(
        'push', help='update a component and push to git repo')
    push_parser.add_argument(
        'files',
        nargs='+',
        help='update the component to match the one on the current project')

    parser.set_defaults(action="list")

    return parser.parse_args()
