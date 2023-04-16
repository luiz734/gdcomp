import os
from component import Component


class ComponentManager():

    def __init__(self, components_path) -> None:
        self.components_path = components_path
        self.current_dir = os.getcwd()

        # self.components = ....
        self._init_components()

    def _init_components(self):
        if not os.path.exists('project.godot'):
            print(
                'Error: "project.godot" file not found in current directory. Please make sure you are running this command in a directory that contains the "project.godot" file.'
            )
            exit(1)

        components_set = set()
        self.get_component_set(component_set=components_set,
                               current_dir=self.components_path)

        components = []
        for c in components_set:
            new_comp = Component(c)
            components.append(new_comp)

        self.components = sorted(components, key=lambda x: x.base_name)

    def get_component_set(self, component_set, current_dir):
        os.chdir(current_dir)
        files_and_dirs = [f for f in os.listdir('.')]

        for f in files_and_dirs:
            item_path = os.path.join(current_dir, f)
            if os.path.isfile(item_path):
                try:
                    base_name = f.split(".")[0]
                except IndexError:
                    print("Skiping invalid file in {} or bad naming".format(
                        current_dir))
                relpath = os.path.relpath(current_dir, self.components_path)
                component_set.add(os.path.join(relpath, base_name))

            elif os.path.isdir(item_path):
                subdir_path = current_dir + "/{}".format(f)
                self.get_component_set(component_set, subdir_path)
            else:
                print("this shouldnt be printed")
