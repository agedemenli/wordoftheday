from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('randomword/', include('randomword.urls')),
    path('admin/', admin.site.urls),
]