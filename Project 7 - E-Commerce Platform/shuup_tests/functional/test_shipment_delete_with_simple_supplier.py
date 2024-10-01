 
import pytest
import random

from shuup.core.models import Shipment
from shuup.testing.factories import create_order_with_product, create_product, get_default_shop
from shuup_tests.simple_supplier.utils import get_simple_supplier


@pytest.mark.django_db
def test_simple_supplier(rf):
    supplier = get_simple_supplier()
    shop = get_default_shop()
    product = create_product("simple-test-product", shop)
    ss = supplier.get_stock_status(product.pk)
    assert ss.logical_count == 0
    num = random.randint(100, 500)
    supplier.adjust_stock(product.pk, +num)
    assert supplier.get_stock_status(product.pk).logical_count == num

    # Create order
    order = create_order_with_product(product, supplier, 10, 3, shop=shop)
    quantities = order.get_product_ids_and_quantities()
    pss = supplier.get_stock_status(product.pk)
    assert pss.logical_count == (num - quantities[product.pk])
    assert pss.physical_count == num
    # Create shipment

    shipment = order.create_shipment_of_all_products(supplier)
    assert isinstance(shipment, Shipment)
    pss = supplier.get_stock_status(product.pk)
    assert pss.logical_count == (num - quantities[product.pk])
    assert pss.physical_count == (num - quantities[product.pk])

    # Delete shipment
    with pytest.raises(NotImplementedError):
        shipment.delete()
    shipment.soft_delete()
    assert shipment.is_deleted()
    pss = supplier.get_stock_status(product.pk)
    assert pss.logical_count == (num - quantities[product.pk])
    assert pss.physical_count == (num)
