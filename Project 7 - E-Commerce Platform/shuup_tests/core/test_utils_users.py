   
import pytest

from shuup.core.utils.users import is_user_all_seeing, toggle_all_seeing_for_user


@pytest.mark.django_db
def test_is_user_all_seeing(rf, admin_user):
    assert not is_user_all_seeing(admin_user)
    toggle_all_seeing_for_user(admin_user)
    assert is_user_all_seeing(admin_user)
    toggle_all_seeing_for_user(admin_user)
    assert not is_user_all_seeing(admin_user)
