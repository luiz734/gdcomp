import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gdcomp",
        description="Handle godot components",
        epilog="Text at the bottom of help",
    )

    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    subparsers.add_parser("ls", help="list avaliable components")

    subparsers.add_parser("config", help="show the config options")

    add_parser = subparsers.add_parser("add", help="add a component to the project")
    add_parser.add_argument("base_name", help="Components(s) to add")

    push_parser = subparsers.add_parser(
        "push", help="update a component and push to git repo"
    )
    push_parser.add_argument(
        "base_name", help="update the component to match the one on the current project"
    )

    parser.set_defaults(action="ls")

    return parser.parse_args()
