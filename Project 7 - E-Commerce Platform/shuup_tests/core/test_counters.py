 
import pytest
from django.core.exceptions import ObjectDoesNotExist

from shuup.core.models import Counter, CounterType


@pytest.mark.django_db
def test_counters():
    for counter_id in (CounterType.ORDER_REFERENCE,):
        try:
            initial = Counter.objects.get(id=CounterType.ORDER_REFERENCE).value
        except ObjectDoesNotExist:
            initial = 0

        last = None
        for x in range(51):
            last = Counter.get_and_increment(counter_id)

        assert last == initial + 50
        assert Counter.objects.get(id=CounterType.ORDER_REFERENCE).value == initial + 51
