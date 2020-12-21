from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('update/', views.update, name='update'),
    re_path(r'^control/(?P<parm_mac>[\s\S])/(?P<parm_mode>[od].{1,})$', views.mode, name='mode'),
    re_path(r'^control/(?P<parm_mac>[\s\S])/(?:speed-(?P<parm_speed>[0-9]*))$', views.change_speed, name='change_speed'),
]
