 
import pytest

from shuup.notify.actions import AddNotification
from shuup.notify.base import TemplatedBinding
from shuup.notify.enums import ConstantUse
from shuup.notify.script import Context


def test_templated_binding_security():
    with pytest.raises(ValueError):
        tb = TemplatedBinding("x", constant_use=ConstantUse.VARIABLE_ONLY)

    with pytest.raises(ValueError):
        tb = TemplatedBinding("y", constant_use=ConstantUse.VARIABLE_OR_CONSTANT)


def test_templated_binding_syntax_errors_swallowed():
    tb = TemplatedBinding("z", constant_use=ConstantUse.CONSTANT_ONLY)
    assert tb.get_value(Context(), {"constant": "{{"}) == "{{"


def test_bind_verification():
    with pytest.raises(ValueError):
        AddNotification({})  # add_notification requires a binding for message
