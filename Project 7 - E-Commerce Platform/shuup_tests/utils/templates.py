 
from copy import deepcopy


def get_templates_setting_for_specific_directories(old_templates_setting, directories):
    templates_setting = deepcopy(old_templates_setting)
    for engine in templates_setting:
        engine["APP_DIRS"] = False
        engine["DIRS"] = directories
    return templates_setting
