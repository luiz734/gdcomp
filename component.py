import os
import shutil
import subprocess


class Component:

    def __init__(self, project_path, components_path, relative_path) -> None:
        self.root_dir = project_path
        self.relative_path = relative_path
        self.components_dir = components_path

        self.base_name = os.path.basename(relative_path)
        self.scene_file_path = '{full_path}.tscn'.format(
            full_path=os.path.join(components_path, relative_path))
        self.script_file_path = '{full_path}.gd'.format(
            full_path=os.path.join(components_path, relative_path))

    def commit(self):
        # changes the dir so it can use git
        os.chdir(self.root_dir)

        try:
            git_add_command = ['git', 'add', self.script_file_path]
            result_add = subprocess.run(
                git_add_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            print("Commit Message: ", end="")
            commit_msg = input()
            git_commit_command = ['git', 'commit', '-m', commit_msg]
            result_commit = subprocess.run(
                git_commit_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            print("{} updated!".format(self.base_name))

        except subprocess.CalledProcessError as e:
            print('Git command failed with return code:', e.returncode)
            print('Git command error:', e.stderr)
            print('(did you make any changes before commit?)')

    def copy_to(self, dst_components_dir):
        if not os.path.exists(dst_components_dir):
            os.makedirs(dst_components_dir)

        # new dirs created based on the relative path
        dirs_to_create = os.path.join(dst_components_dir,
                                      os.path.dirname(self.relative_path))
        os.makedirs(dirs_to_create, exist_ok=True)

        dst_script_full_path = os.path.join(
            dst_components_dir, self.relative_path) + ".gd"
        shutil.copy(self.script_file_path, dst_script_full_path)

        # some scripts doesnt contain scenes
        try:
            dst_scene_full_path = os.path.join(
                dst_components_dir, self.relative_path) + ".tscn"
            shutil.copy(self.scene_file_path, dst_scene_full_path)
        except FileExistsError:
            print("Skiping missing scene file")
            pass