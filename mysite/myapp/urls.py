from django.conf.urls import url, include

from myapp.views import myapp_home


urlpatterns = [
    url('', myapp_home, name='myapp_home')
]
