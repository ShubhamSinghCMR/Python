 
import mock

from shuup.admin.browser_config import DefaultBrowserConfigProvider
from shuup.admin.template_helpers.shuup_admin import get_config
from shuup.testing.utils import apply_request_middleware
from shuup.utils.django_compat import reverse


def test_get_config(rf, admin_user):
    request = apply_request_middleware(rf.get("/"), user=admin_user)
    context = dict(request=request)
    config = get_config(context)
    for key, url in DefaultBrowserConfigProvider.get_browser_urls(request).items():
        if isinstance(url, tuple):
            assert config["browserUrls"][key] == reverse(url[0], args=url[1], kwargs=url[2])
        else:
            assert config["browserUrls"][key] == reverse(url)
    assert "minSearchInputLength" in DefaultBrowserConfigProvider.get_gettings(request).keys()
