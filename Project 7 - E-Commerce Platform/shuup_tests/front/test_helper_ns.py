   
from shuup.apps.provides import override_provides
from shuup.front.templatetags.shuup_front import _get_helpers


class TestNs:
    name = "badgers"

    def snake(self):
        return True


def test_extendable_helper_ns():
    with override_provides("front_template_helper_namespace", ["%s:TestNs" % __name__]):
        ns = _get_helpers()
        assert ns.badgers.snake()
