import os
from component import Component


def handle(files, manager):
    manager.components[11].copy_to(manager.current_dir)

    print(c.base_name for c in manager.components)
