from django.urls import path, re_path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.course_list, name='course_list'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.course_detail, name='course_detail'),
    path('search/', views.course_search, name='course_search'),
]
