 
import pytest

from shuup.notify.base import Event
from shuup_tests.notify.fixtures import ATestEvent, get_initialized_test_event


@pytest.mark.django_db
def test_event_init():
    assert get_initialized_test_event().variable_values


def test_extra_vars_fails():
    with pytest.raises(ValueError):
        ATestEvent(not_valid=True)


def test_missing_vars_fails():
    with pytest.raises(ValueError):
        ATestEvent(just_some_text="Hello")


def test_init_empty_fails():
    with pytest.raises(ValueError):
        Event()


def test_auto_name():
    assert ATestEvent.name == "Test Event"
