from component_manager import ComponentManager
from config import Config
import argparser
import actions
import os


class GDComp:
    def __init__(self) -> None:
        self.config = Config()

        current_dir = os.getcwd()

        self.project_manager = ComponentManager(
            current_dir, os.path.join(current_dir, "components")
        )
        self.components_manager = ComponentManager(
            self.config.components_dir, self.config.components_dir
        )
        self.args = argparser.parse_args()

    def run(self):
        self.action = self.args.action

        # gdcomp add <component>
        if self.action == "add":
            actions.handle_add(
                self.args.base_name, self.components_manager, self.project_manager
            )

        # gdcomp push <project_component>
        elif self.action == "push":
            actions.handle_push(
                self.args.base_name, self.components_manager, self.project_manager
            )

        # gdcomp ls [-p]
        elif self.action == "ls":
            to_highlight = []
            if self.args.project_dir:
                actions.handle_list(self.project_manager, to_highlight)
            else:
                to_highlight = self.project_manager.get_basenames()
                actions.handle_list(self.components_manager, to_highlight)

        # gdcomp config
        elif self.action == "config":
            actions.handle_config(
                self.config, self.components_manager, self.project_manager
            )
