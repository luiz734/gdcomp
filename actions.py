import os
from component import Component
from fuzzywuzzy import fuzz, process


def handle_add(file_basename, components_manager, project_manager):
    comp_to_add = components_manager.find_fuzzy_interactivly(file_basename)
    comp_to_add.copy_to(project_manager.components_dir)
    print("Component {} added".format(comp_to_add.base_name))

    # components_manager.components[11].copy_to(project_manager.components_dir)


def handle_list(manager):
    for c in manager.components:
        print("{}".format(c.base_name))


def handle_push(file_basename, components_manager, project_manager):
    src = dst = None

    src = project_manager.find_fuzzy_interactivly(file_basename)
    dst = components_manager.find_exactly(file_basename)

    if not src:
        print(
            "{} not found in {}".format(file_basename, project_manager.components_dir)
        )
        exit(1)

    if not dst:
        answer = input(
            "{} found in project but not in components dir. Add? (Y/n) ".format(
                file_basename
            )
        )
        if answer in ["y", "Y", ""]:
            src.copy_to(components_manager.components_dir)
            components_manager.rebase()
            dst = components_manager.find_exactly(src.base_name)
            dst.commit()
        else:
            print("Aborting. Nothing change")
    else:
        src.copy_to(dst.components_dir)
        dst.commit()


def handle_config(components_manager, project_manager):
    print("Components: {}".format(components_manager.components_dir))
    print("Current Project: {}".format(project_manager.project_dir))
    print("Current Components: {}".format(project_manager.components_dir))
