from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("archive", views.archive, name="archive"),
    path("delete/<int:entry_id>", views.delete, name="delete"),
    path("archive_entry/<int:entry_id>", views.archive_entry, name="archive_entry"),
    path("unarchive_entry/<int:entry_id>", views.unarchive_entry, name="unarchive_entry"),
]