 

from django.conf.urls import url

urlpatterns = [
    url("test/(?P<arg>.+)/$", (lambda: 0), name="test"),
]
