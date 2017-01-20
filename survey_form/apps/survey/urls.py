from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_survey$', views.submit),
    url(r'^post$', views.post)
]
