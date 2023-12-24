from django.urls import path

from project.store import views


urlpatterns = [
    path("", views.store, name="main page"),
    path("phones/", views.phones, name="page about phones"),
    path("cases/", views.cases, name="page about cases"),
]
