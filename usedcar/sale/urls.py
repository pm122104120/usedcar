from django.conf.urls import url
from sale import views


urlpatterns = [
    url(r'^upimg',views.Upimg,name='upimg'),
]