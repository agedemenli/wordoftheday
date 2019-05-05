from django.urls import path
from . import views

urlpatterns = [
    #url(r'^company/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    path('<str:lang>', views.index, name='index'),
]