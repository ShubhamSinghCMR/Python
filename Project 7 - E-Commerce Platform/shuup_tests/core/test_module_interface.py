 
from __future__ import unicode_literals

import pytest

from shuup.core.models import Supplier


@pytest.mark.django_db
def test_module_interface_for_scandinavian_letters(rf):
    supplier = Supplier.objects.create(identifier="module_interface_test", name="ääääööööååå")

    assert isinstance(supplier, Supplier)
    assert not supplier.modules
    assert "%r" % supplier

    supplier.delete()
