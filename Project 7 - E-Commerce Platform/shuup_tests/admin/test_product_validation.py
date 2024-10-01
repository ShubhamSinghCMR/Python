   
import pytest

from shuup.admin.modules.products.issues import ProductValidationIssue
from shuup.admin.modules.products.validators import AdminProductValidator
from shuup.testing.admin_product_validator import TestAdminProductValidator
from shuup.testing.factories import create_product, get_default_shop, get_default_supplier
from shuup_tests.utils import printable_gibberish


@pytest.mark.django_db
def test_product_validation(rf, admin_user):
    """
    Test for Product validation related classes: AdminProductValidator and ProductValidationIssue.
    """
    shop = get_default_shop()
    supplier = get_default_supplier()
    product = create_product(printable_gibberish(), shop=shop, supplier=supplier, default_price=50)
    shop_product = product.get_shop_instance(shop)

    validator = TestAdminProductValidator
    validation_issues = []
    for issue in validator.get_validation_issues(shop_product, shop, admin_user, supplier):
        validation_issues.append(issue)

    validation_issues = sorted(validation_issues, key=lambda x: x.get_issue_type_priority())
    error_issue = validation_issues[0]
    assert error_issue.issue_type == "error"
    assert error_issue.code == "1200"
    assert isinstance(error_issue.code, str) or error_issue.code is None
    assert isinstance(error_issue.issue_type, str)
    assert error_issue.get_issue_type_priority() == 1
    assert error_issue.get_alert_type() == "danger"

    with pytest.raises(ValueError):
        issue = ProductValidationIssue("Test message", "invalid", "1000", False)

    base_validator = AdminProductValidator
    for issue in base_validator.get_validation_issues(shop_product, shop, admin_user, supplier):
        assert issue is None
