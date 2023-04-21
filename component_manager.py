import os
from component import Component

ALLOWED_TYPES = ["gd", "tscn"]


class ComponentManager():

    def __init__(self, project_path, components_path) -> None:
        self.project_path = project_path
        self.components_path = components_path
        self._init_components()

    def _init_components(self):
        components_set = set()
        self.get_component_set(component_set=components_set,
                               current_dir=self.components_path)

        components = []
        for relative_path in components_set:
            new_comp = Component(
                self.project_path, self.components_path, relative_path)
            components.append(new_comp)

        self.components = sorted(components, key=lambda x: x.base_name)

    def get_component_set(self, component_set, current_dir):
        os.chdir(current_dir)
        files_and_dirs = [f for f in os.listdir('.')]

        for f in files_and_dirs:
            item_path = os.path.join(current_dir, f)
            if os.path.isfile(item_path):
                try:
                    splited = f.split(".")
                    base_name = splited[0]
                    filetype = splited[len(splited) - 1]
                except IndexError:
                    print("Skiping invalid file in {} or bad naming".format(
                        current_dir))
                if filetype in ALLOWED_TYPES:
                    relpath = os.path.relpath(current_dir, self.components_path)
                    component_set.add(os.path.join(relpath, base_name))

            elif os.path.isdir(item_path):
                subdir_path = current_dir + "/{}".format(f)
                self.get_component_set(component_set, subdir_path)
            else:
                print("this shouldnt be printed")
