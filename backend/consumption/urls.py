from django.urls import path
from .views import consumption_view

urlpatterns = [
    path('consumption/', consumption_view),
]
