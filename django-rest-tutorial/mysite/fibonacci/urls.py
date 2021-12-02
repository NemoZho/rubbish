from django.urls import path, re_path

from .views import PostView

urlpatterns = [
    re_path(r'^fibonacci/?$', PostView.as_view()),
]
