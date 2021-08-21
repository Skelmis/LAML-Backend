from django.urls import path, include

from base.views import index

urlpatterns = [
    path("", index),
]
