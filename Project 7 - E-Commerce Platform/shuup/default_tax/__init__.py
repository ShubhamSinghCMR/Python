   
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = __name__
    verbose_name = _("Shuup Default Tax")
    label = "default_tax"

    provides = {
        "tax_module": ["shuup.default_tax.module:DefaultTaxModule"],
        "admin_module": ["shuup.default_tax.admin_module:TaxRulesAdminModule"],
    }


default_app_config = __name__ + ".AppConfig"
