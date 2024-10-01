   
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup.tasks"
    label = "shuup_tasks"
    provides = {
        "admin_module": ["shuup.tasks.admin_module.TaskAdminModule", "shuup.tasks.admin_module.TaskTypeAdminModule"]
    }
