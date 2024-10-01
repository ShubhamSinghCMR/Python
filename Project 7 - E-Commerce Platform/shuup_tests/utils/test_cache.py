 
from django.test import override_settings

from shuup.core import cache


def test_cache_api():
    with override_settings(
        CACHES={
            "default": {
                "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
                "LOCATION": "test_configuration_cache",
            }
        }
    ):
        cache.init_cache()

        key = "test_prefix:123"
        value = "456"
        cache.set(key, value)
        assert cache.get(key) == value
        cache.bump_version(key)
        assert cache.get(key, default="derp") == "derp"  # version was bumped, so no way this is there
        cache.set(key, value)
        assert cache.get(key) == value
