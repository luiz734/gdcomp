import os
from component import Component
from fuzzywuzzy import fuzz, process


def handle_add(file_basename, components_manager, project_manager):
    possible_targets = components_manager.get_basenames()
    best_match = process.extractOne(file_basename, possible_targets)[0]
    if best_match != file_basename:
        answer = input("Did you mean {}? (y/n) ".format(best_match))
        if not answer in ["y", "Y"]:
            print("{basename} not found in {dir}".format(
                basename=file_basename, dir=components_manager.components_path))
            print("Run <command> or <command> ls to see all options")
            exit(1)

    for c in components_manager.components:
        if c.base_name == best_match:
            c.copy_to(project_manager.components_path)
            print("Component {} added".format(best_match))
            break

    # components_manager.components[11].copy_to(project_manager.components_path)


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
    if not dst:
        print("{} found in project but not in components dir. Add? (y/n) ".format(file_basename), end="")
        answer = input()
        if answer in ["y", "Y"]:
            src.copy_to(components_manager.components_path)
            dst.commit()
        else:
            print("Aborting. Nothing change")
    else:
        src.copy_to(dst.components_dir)
        dst.commit()
