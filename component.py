import os
import shutil

GODOT_COMPONENTS_DIR = "/home/tohru/Drive/godot/components"


class Component:

    def __init__(self, relative_path) -> None:
        self.relative_path = relative_path
        self.base_name = os.path.basename(relative_path)
        self.full_path = os.path.join(GODOT_COMPONENTS_DIR, relative_path)

    def copy_to(self, dst_dir):
        scene_file = '{full_path}.tscn'.format(full_path=self.full_path)
        script_file = '{full_path}.gd'.format(full_path=self.full_path)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        full_scene_dst = os.path.join(dst_dir, self.relative_path) + ".tscn"
        full_script_dst = os.path.join(dst_dir, self.relative_path) + ".gd"

        dirs_to_create = os.path.join(dst_dir,
                                      os.path.dirname(self.relative_path))
        os.makedirs(dirs_to_create, exist_ok=True)

        shutil.copy(scene_file, full_scene_dst)
        shutil.copy(script_file, full_script_dst)
