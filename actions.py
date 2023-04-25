import os
from component import Component
from fuzzywuzzy import fuzz, process
import display


def handle_add(file_basename, components_manager, project_manager):
    comp_to_add = components_manager.find_fuzzy_interactivly(file_basename)
    comp_to_add.copy_to(project_manager.components_dir)
    display.success("Component {} added".format(comp_to_add.base_name))


def handle_list(manager):
    for c in manager.components:
        display.text("{}".format(c.base_name))


def handle_push(file_basename, components_manager, project_manager):
    src = dst = None
    src = project_manager.find_fuzzy_interactivly(file_basename)
    dst = components_manager.find_exactly(src.base_name)

    if not src:
        display.warn(
            "{} not found in {}".format(file_basename, project_manager.components_dir)
        )
        exit(1)

    if not dst:
        answer = input(
            "{} found in project but not in components dir. Add? (Y/n) ".format(
                src.base_name
            )
        )
        if answer in ["y", "Y", ""]:
            src.copy_to(components_manager.components_dir)
            components_manager.rebase()
            dst = components_manager.find_exactly(src.base_name)
            dst.commit()
        else:
            display.warn("Aborting. Nothing change")
    else:
        src.copy_to(dst.components_dir)
        dst.commit()


def handle_config(config, components_manager, project_manager):
    display_msg = """
Components: {comp_dir}
Current Project: {proj_dir}
Current Components: {proj_comp_dir}
\nConfig File: {config_path}
{config_content}""".format(
        comp_dir=components_manager.components_dir,
        proj_dir=project_manager.project_dir,
        proj_comp_dir=project_manager.components_dir,
        config_path=config.path,
        config_content=config.get_all_as_str(),
    )
    display.text(display_msg)
