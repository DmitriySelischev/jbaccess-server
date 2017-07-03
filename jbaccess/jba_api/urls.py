from django.conf.urls import url, include

urlpatterns = [
    url(r'^heartbeat/?', include('jba_api.heartbeat.urls')),
    url(r'^calc/?', include('jba_api.calculator.urls')),
    url(r'^security/?', include('jba_api.security.urls')),
    url(r'^controllers/?', include('jba_api.controllers.urls')),
    url(r'^doors/?', include('jba_api.doors.urls')),
    url(r'^places/?', include('jba_api.places.urls')),
    url(r'^person/?', include('jba_api.person.urls')),
    url(r'^keys/?', include('jba_api.keys.urls'))
]
