import os
from component import Component
from fuzzywuzzy import fuzz, process
import display

ALLOWED_TYPES = ["gd", "tscn"]


class ComponentManager:
    def __init__(self, project_dir, components_dir) -> None:
        self.project_dir = project_dir
        self.components_dir = components_dir
        self._init_components()

    def get_basenames(self):
        return [c.base_name for c in self.components]

    def rebase(self):
        self._init_components()

    def find_exactly(self, base_name):
        for c in self.components:
            if c.base_name == base_name:
                return c
        return None

    def find_fuzzy_interactivly(self, base_name):
        possible_targets = self.get_basenames()
        try:
            best_match = process.extractOne(base_name, possible_targets)[0]
        except TypeError:
            display.text(
                "Nothing matches {}. Run <command> ls to see all avaliable components".format(
                    base_name
                )
            )
            exit(1)
        if best_match != base_name:
            answer = input("Did you mean {}? (Y/n) ".format(best_match))
            if not answer in ["y", "Y", ""]:
                display.text(
                    "{base_name} not found in {dir}".format(
                        base_name=base_name, dir=self.components_dir
                    )
                )
                display.text(
                    "Run <command> or <command> ls to see all avaliable components"
                )
                exit(1)

        for c in self.components:
            if c.base_name == best_match:
                return c

    # components_manager.components[11].copy_to(project_manager.components_dir)

    def _init_components(self):
        if not os.path.exists(self.components_dir):
            display.warn("Creating missing dir {}".format(self.components_dir))
            os.makedirs(self.components_dir, exist_ok=False)

        components_set = set()
        self.get_component_set(
            component_set=components_set, current_dir=self.components_dir
        )

        components = []
        for relative_path in components_set:
            new_comp = Component(self.project_dir, self.components_dir, relative_path)
            components.append(new_comp)

        self.components = sorted(components, key=lambda x: x.base_name)

    def get_component_set(self, component_set, current_dir):
        os.chdir(current_dir)
        files_and_dirs = [f for f in os.listdir(".")]

        for f in files_and_dirs:
            item_path = os.path.join(current_dir, f)
            if os.path.isfile(item_path):
                try:
                    splited = f.split(".")
                    base_name = splited[0]
                    filetype = splited[len(splited) - 1]
                except IndexError:
                    display.warn(
                        "Skiping {file} invalid file in {dir} or bad naming".format(
                            file=f, dir=current_dir
                        )
                    )
                if filetype in ALLOWED_TYPES:
                    relpath = os.path.relpath(current_dir, self.components_dir)
                    component_set.add(os.path.join(relpath, base_name))

            elif os.path.isdir(item_path):
                subdir_path = current_dir + "/{}".format(f)
                self.get_component_set(component_set, subdir_path)
            else:
                display.warn("this shouldnt be display.texted")
