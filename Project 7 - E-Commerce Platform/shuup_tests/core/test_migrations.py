 
import pytest
from django.core.management import call_command
from six import StringIO


@pytest.mark.django_db
def test_makemigrations():
    out = StringIO()
    call_command("makemigrations", "--dry-run", stdout=out)
    assert "No changes detected" in out.getvalue()
