from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_points, name='post_list'),
]