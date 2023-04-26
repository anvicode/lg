from django.urls import path, re_path

from .views import *  # noqa: F403

urlpatterns = [
    path("", index, name="home"),  # noqa: F405
    path("cats/<int:catid>/", categories, name="cats"),  # noqa: F405
    re_path(r"^archive/(?P<year>[0-9]{4})/", archive, name="archive"),  # noqa: F405
]
