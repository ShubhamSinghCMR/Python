 
from shuup.apps import AppConfig


class AppConfig(AppConfig):
    name = "shuup_tests.core"
    label = "shuup_tests_core"

    provides = {
        "module_test_module": [
            "shuup_tests.core.module_test_module:ModuleTestModule",
            "shuup_tests.core.module_test_module:AnotherModuleTestModule",
        ]
    }


default_app_config = "shuup_tests.core.AppConfig"
