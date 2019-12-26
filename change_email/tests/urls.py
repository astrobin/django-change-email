from django.conf.urls.defaults import *

urlpatterns = (
    url(r'^account/', include('change_email.urls')),
)
