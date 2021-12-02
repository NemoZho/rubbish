from django.urls import path, re_path

from .views import EchoView

urlpatterns = [
    re_path(r'^tutorial/?$', EchoView.as_view()),
]
