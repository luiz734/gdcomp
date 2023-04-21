import os
from component import Component


def handle_add(files, components_manager, project_manager):
    components_manager.components[11].copy_to(project_manager.components_path)


def handle_list(manager):
    for c in manager.components:
        print("{}".format(c.base_name))


def handle_push(file_basename, components_manager, project_manager):
    src = dst = None

    for c in project_manager.components:
        if c.base_name == file_basename:
            src = c
    for c in components_manager.components:
        if c.base_name == file_basename:
            dst = c

    src.copy_to(dst.components_dir)
    dst.commit()
