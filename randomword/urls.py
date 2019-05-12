from django.urls import path
from . import views

urlpatterns = [
    # You can call it like /randomword/en
    # Here, the string 'en' is being passed to the view as a parameter.
    path('<str:lang>', views.index, name='index'),
]