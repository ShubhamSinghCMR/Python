 
from shuup_tests.utils import replace_urls


def get_admin_only_urls():
    from django.conf.urls import include, url

    from shuup.admin.urls import get_urls

    class FauxUrlPatternsModule:
        app_name = "shuup_admin"
        urlpatterns = get_urls()

    return [
        url(r"^sa/", include(FauxUrlPatternsModule, namespace="shuup_admin")),
    ]


def admin_only_urls():
    return replace_urls(get_admin_only_urls())
