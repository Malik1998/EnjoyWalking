from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create', views.add_point, name='add_point'),
    url(r'^$', views.post_points, name='post_list'),
]