from django.conf.urls import url
from .controllers import *

urlpatterns = [
    url(r'^$', PersonController.as_view()),
    url(r'^(?P<id>\d+)$', PersonRUDController.as_view())
]