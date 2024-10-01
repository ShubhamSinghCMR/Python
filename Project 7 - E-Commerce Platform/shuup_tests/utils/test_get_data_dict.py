   
import json
import pytest

from shuup.testing import factories
from shuup.utils.models import get_data_dict


@pytest.mark.django_db
def test_get_data_dict_force_value_with_json_serializer():
    product = factories.get_default_product()

    with pytest.raises(TypeError):
        json.dumps(get_data_dict(product))

    json.dumps(get_data_dict(product, force_text_for_value=True))
