from django.contrib import admin
from django.urls import path

from publish.views import view_post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<slug:slug>/", view_post, name="view_post"),
]
